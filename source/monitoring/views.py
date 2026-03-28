import json
import math
import requests as http_requests
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from django.db.models import Count, Avg, Q
from django.db.models.functions import TruncMonth
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
from .models import WaterSample, Alert, VillageProfile
from .forms import WaterSampleForm
from .utils import send_sms_alert


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'monitoring/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


def dashboard(request):
    # --- KPI Summary Metrics ---
    total_samples = WaterSample.objects.count()
    high_risk_count = WaterSample.objects.filter(risk_score__gt=70).count()
    moderate_risk_count = WaterSample.objects.filter(
        risk_score__gte=30, risk_score__lte=70
    ).count()
    safe_count = WaterSample.objects.filter(risk_score__lt=30).count()
    active_alerts = Alert.objects.filter(resolved=False).count()
    resolved_alerts = Alert.objects.filter(resolved=True).count()

    ecoli_rate = 0
    safe_pct = 0
    if total_samples > 0:
        ecoli_rate = round(
            WaterSample.objects.filter(
                ecoli_present=True
            ).count() / total_samples * 100, 1
        )
        safe_pct = round(safe_count / total_samples * 100, 1)

    # --- Monthly Trend Data (last 12 months) ---
    monthly_qs = (
        WaterSample.objects
        .annotate(month=TruncMonth('date_collected'))
        .values('month')
        .annotate(
            total=Count('id'),
            high_risk=Count(
                'id',
                filter=Q(risk_score__gt=70)
            ),
        )
        .order_by('month')
    )
    # Build month labels and data arrays
    month_labels = []
    month_totals = []
    month_high_risk = []
    for entry in monthly_qs:
        if entry['month']:
            month_labels.append(entry['month'].strftime('%b %Y'))
            month_totals.append(entry['total'])
            month_high_risk.append(entry['high_risk'])

    # --- Cases by Water Source ---
    source_qs = (
        WaterSample.objects
        .values('water_source')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    source_labels = [s['water_source'] for s in source_qs]
    source_counts = [s['count'] for s in source_qs]

    # --- Cases by District ---
    district_qs = (
        WaterSample.objects
        .values('district')
        .annotate(
            total=Count('id'),
            high_risk=Count(
                'id',
                filter=Q(risk_score__gt=70)
            ),
        )
        .order_by('-total')[:10]
    )
    district_labels = [d['district'] for d in district_qs]
    district_totals = [d['total'] for d in district_qs]
    district_high_risk = [d['high_risk'] for d in district_qs]

    # --- Recent Alerts ---
    alerts = Alert.objects.filter(
        resolved=False
    ).order_by('-created_at')[:5]

    # --- High Risk Villages ---
    risk_villages = (
        WaterSample.objects.filter(risk_score__gt=70)
        .values('village', 'district')
        .annotate(risk_count=Count('id'))
        .order_by('-risk_count')[:5]
    )

    # --- Radar Chart Data ---
    radar_data = {
        'avg_turbidity': round(
            WaterSample.objects.aggregate(
                avg=Avg('turbidity')
            )['avg'] or 0, 2
        ),
        'avg_ph': round(
            WaterSample.objects.aggregate(
                avg=Avg('ph')
            )['avg'] or 7, 2
        ),
        'ecoli_rate': ecoli_rate,
        'avg_nitrate': round(
            WaterSample.objects.aggregate(
                avg=Avg('nitrate_level')
            )['avg'] or 0, 2
        ),
        'avg_risk': round(
            WaterSample.objects.aggregate(
                avg=Avg('risk_score')
            )['avg'] or 0, 2
        ),
    }

    # --- Recent Samples (Activity Feed) ---
    recent_samples = WaterSample.objects.order_by(
        '-date_collected'
    )[:5]

    context = {
        'total_samples': total_samples,
        'high_risk_count': high_risk_count,
        'moderate_risk_count': moderate_risk_count,
        'safe_count': safe_count,
        'active_alerts': active_alerts,
        'resolved_alerts': resolved_alerts,
        'ecoli_rate': ecoli_rate,
        'safe_pct': safe_pct,
        'alerts': alerts,
        'risk_villages': risk_villages,
        'radar_data': radar_data,
        'recent_samples': recent_samples,
        # JSON-serialized chart data
        'month_labels': json.dumps(month_labels),
        'month_totals': json.dumps(month_totals),
        'month_high_risk': json.dumps(month_high_risk),
        'source_labels': json.dumps(source_labels),
        'source_counts': json.dumps(source_counts),
        'district_labels': json.dumps(district_labels),
        'district_totals': json.dumps(district_totals),
        'district_high_risk': json.dumps(district_high_risk),
    }
    return render(request, 'monitoring/dashboard.html', context)


def submit_sample(request):
    if request.method == 'POST':
        form = WaterSampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            if request.user.is_authenticated:
                sample.user = request.user
            sample.save()
            return render(request, 'monitoring/sample_result.html', {'sample': sample})
    else:
        form = WaterSampleForm()
    return render(request, 'monitoring/submit_sample.html', {'form': form})


def alert_list(request):
    alerts = Alert.objects.all().order_by('-created_at')
    return render(request, 'monitoring/alerts.html', {'alerts': alerts})


def resolve_alert(request, alert_id):
    if request.method == 'POST':
        alert = get_object_or_404(Alert, id=alert_id)
        alert.resolved = True
        if request.user.is_authenticated:
            alert.resolved_by = request.user
        alert.save()
    return redirect('alert_list')


def send_sms(request, sample_id):
    if request.method == 'POST':
        sample = get_object_or_404(WaterSample, id=sample_id)
        if not sample.phone_number:
            return JsonResponse({'success': False, 'error': 'No phone number provided for this sample.'})

        success = send_sms_alert(
            phone_number=sample.phone_number,
            village=sample.village,
            cause=sample.cause,
            remedy=sample.remedy
        )

        if success:
            return JsonResponse({'success': True, 'message': 'SMS sent successfully.'})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to send SMS. Check terminal logs for details.'})

    return JsonResponse({'success': False, 'error': 'Invalid request method.'})


def home(request):
    """Landing page with live stats."""
    total_samples = WaterSample.objects.count()
    active_alerts = Alert.objects.filter(resolved=False).count()
    safe_count = WaterSample.objects.filter(risk_score__lt=30).count()
    safe_pct = round(
        safe_count / total_samples * 100, 1
    ) if total_samples > 0 else 100
    districts_count = WaterSample.objects.values(
        'district'
    ).distinct().count()

    context = {
        'total_samples': total_samples,
        'active_alerts': active_alerts,
        'safe_pct': safe_pct,
        'districts_count': districts_count,
    }
    return render(request, 'monitoring/home.html', context)


# --- HACKATHON PIVOT FEATURES ---

@csrf_exempt
def twilio_webhook(request):
    """HACKATHON PIVOT: Offline SMS Fallback using Twilio."""
    if request.method == 'POST':
        body = request.POST.get('Body', '').strip().lower()
        sender = request.POST.get('From', '')
        
        # Simple parser for hackathon demo. Expected format: "Village: Sulur, pH: 6.5, Turbidity: 10"
        try:
            parts = dict(item.split(':') for item in body.split(','))
            village_name = parts.get('village', '').strip().title()
            ph_val = float(parts.get('ph', 7.0))
            turbidity_val = float(parts.get('turbidity', 5.0))
            
            # Log Rapid Sample
            sample = WaterSample.objects.create(
                village=village_name,
                district="Unknown (SMS)",
                latitude=0.0,
                longitude=0.0,
                ph=ph_val,
                turbidity=turbidity_val,
                water_source="SMS Report",
                phone_number=sender
            )
            return HttpResponse('<Response><Message>WSP: Offline sample logged successfully. Risk engine triggered.</Message></Response>', content_type='text/xml')
        except Exception as e:
            return HttpResponse('<Response><Message>WSP Error: Invalid format. Use "Village: X, pH: Y, Turbidity: Z"</Message></Response>', content_type='text/xml')

    return HttpResponse("OK")


def smart_dispatch(request):
    """HACKATHON PIVOT: Smart Dispatch AI prioritizing high-risk areas based on population."""
    alerts = Alert.objects.filter(alert_level='Red').order_by('-created_at')
    dispatch_list = []
    
    for alert in alerts:
        try:
            profile = VillageProfile.objects.get(name=alert.village)
            pop = profile.population
        except VillageProfile.DoesNotExist:
            pop = 5000 # Default assumption
            
        # Triage Score = Risk Score * Population Density Factor 
        triage_score = (alert.risk_score * pop) / 1000
        
        dispatch_list.append({
            'alert': alert,
            'population': pop,
            'triage_score': round(triage_score, 1)
        })
        
    # Sort by highest triage score first
    dispatch_list.sort(key=lambda x: x['triage_score'], reverse=True)
    return render(request, 'monitoring/smart_dispatch.html', {'dispatch_list': dispatch_list})


def dispatch_van(request, alert_id):
    """DISPATCH LIFECYCLE STEP 1: Send recovery team and notify them via SMS."""
    alert = get_object_or_404(Alert, id=alert_id)
    if request.method == 'POST' and not alert.dispatched:
        alert.dispatched = True
        alert.dispatched_at = timezone.now()
        alert.dispatched_team_notified = True
        alert.save()

        # --- SIMULATED SMS TO RECOVERY TEAM ---
        # In production, this would use the Twilio API:
        #   client.messages.create(
        #       body=f"URGENT: Mobile Testing Van dispatched to {alert.village}. Risk: {alert.risk_score}%. Report immediately.",
        #       from_='+1WSPNUMBER', to='+91TEAMLEAD'
        #   )
        team_sms = f"[SMS SENT TO RECOVERY TEAM] URGENT WSP Dispatch: Mobile Testing Van dispatched to {alert.village}, {alert.district}. Contamination Risk: {alert.risk_score}%. Triage Priority: HIGH. Report to site immediately."
        print(team_sms)  # Logged in server console for hackathon demo

    return redirect('smart_dispatch')


def resolve_dispatch(request, alert_id):
    """DISPATCH LIFECYCLE STEP 2: Problem solved. Notify public via SMS."""
    alert = get_object_or_404(Alert, id=alert_id)
    if request.method == 'POST' and alert.dispatched and not alert.resolved:
        alert.resolved = True
        alert.resolved_at = timezone.now()
        alert.public_notified = True
        if request.user.is_authenticated:
            alert.resolved_by = request.user
        alert.save()

        # --- SIMULATED SMS TO PUBLIC ---
        # In production, this would broadcast to all registered phone numbers in the village:
        #   for contact in VillageContacts.objects.filter(village=alert.village):
        #       client.messages.create(
        #           body=f"WSP SAFETY ALERT: Water in {alert.village} has been tested and is now SAFE...",
        #           from_='+1WSPNUMBER', to=contact.phone
        #       )
        public_sms = f"[SMS BROADCAST TO PUBLIC] WSP Safety Update for {alert.village}, {alert.district}: Water contamination issue has been RESOLVED by the government recovery team. Water is now SAFE for consumption. Thank you for your patience. - Dept. of Water Sanitation, TN"
        print(public_sms)  # Logged in server console for hackathon demo

    return redirect('smart_dispatch')


def _haversine(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance (km) between two points on Earth."""
    R = 6371  # Earth radius in km
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dlon / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def nearby_sources(request):
    """Pinpoint user location via IP/GPS and find nearby water sources on a satellite map."""
    RADIUS_KM = 100  # Expanded search radius

    # --- Step 1: Get user IP ---
    x_forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded:
        ip = x_forwarded.split(',')[0].strip()
    else:
        ip = request.META.get('REMOTE_ADDR', '')

    # --- Step 2: Geolocate via ip-api.com ---
    user_lat, user_lon = 11.0168, 76.9558  # Default: Coimbatore
    city, region, country = 'Coimbatore', 'Tamil Nadu', 'India'
    geo_success = False

    private_prefixes = ('127.', '10.', '192.168.', '172.', '::1', 'localhost')
    if ip and not ip.startswith(private_prefixes):
        try:
            resp = http_requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            data = resp.json()
            if data.get('status') == 'success':
                user_lat = data.get('lat', user_lat)
                user_lon = data.get('lon', user_lon)
                city = data.get('city', city)
                region = data.get('regionName', region)
                country = data.get('country', country)
                geo_success = True
        except Exception:
            pass  # Fall back to defaults

    # --- Step 3: Find nearby water samples ---
    nearby = _find_nearby_samples(user_lat, user_lon, RADIUS_KM)

    context = {
        'user_lat': user_lat,
        'user_lon': user_lon,
        'city': city,
        'region': region,
        'country': country,
        'geo_success': geo_success,
        'ip': ip,
        'radius_km': RADIUS_KM,
        'nearby_sources': nearby,
        'nearby_json': json.dumps(nearby),
        'total_nearby': len(nearby),
    }
    return render(request, 'monitoring/nearby_sources.html', context)


def _find_nearby_samples(user_lat, user_lon, radius_km):
    """Find water samples within radius_km of (user_lat, user_lon)."""
    samples = WaterSample.objects.all()
    nearby = []
    for s in samples:
        try:
            dist = _haversine(user_lat, user_lon, s.latitude, s.longitude)
        except (TypeError, ValueError):
            continue
        if dist <= radius_km:
            risk = s.risk_score or 0
            if risk > 70:
                color = 'red'
                level = 'High Risk'
            elif risk >= 30:
                color = 'orange'
                level = 'Moderate'
            else:
                color = 'green'
                level = 'Safe'
            nearby.append({
                'id': s.id,
                'village': s.village,
                'district': s.district,
                'latitude': s.latitude,
                'longitude': s.longitude,
                'distance_km': round(dist, 1),
                'risk_score': round(risk, 1),
                'color': color,
                'level': level,
                'water_source': s.water_source,
                'date': s.date_collected.strftime('%Y-%m-%d') if s.date_collected else '',
            })
    nearby.sort(key=lambda x: x['distance_km'])
    return nearby


def nearby_sources_api(request):
    """JSON API: Re-fetch nearby sources for a given GPS coordinate."""
    lat = float(request.GET.get('lat', 11.0168))
    lon = float(request.GET.get('lon', 76.9558))
    radius = float(request.GET.get('radius', 100))
    nearby = _find_nearby_samples(lat, lon, radius)
    return JsonResponse({'sources': nearby, 'total': len(nearby)})
