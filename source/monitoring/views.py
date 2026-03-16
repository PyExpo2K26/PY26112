from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count, Avg
from django.http import JsonResponse
from .models import WaterSample, Alert
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
    # Summary Metrics
    total_samples = WaterSample.objects.count()
    high_risk_count = WaterSample.objects.filter(risk_score__gt=70).count()
    active_alerts = Alert.objects.filter(resolved=False).count()

    # Recent Alerts
    alerts = Alert.objects.filter(resolved=False).order_by('-created_at')[:5]

    # High Risk Villages (Grouped)
    risk_villages = WaterSample.objects.filter(risk_score__gt=70)\
        .values('village', 'district')\
        .annotate(risk_count=Count('id'))\
        .order_by('-risk_count')[:5]

    # Radar Chart Data (Aggregate Risk Factors)
    radar_data = {
        'avg_turbidity': WaterSample.objects.aggregate(avg=Avg('turbidity'))['avg'] or 0,
        'avg_ph': WaterSample.objects.aggregate(avg=Avg('ph'))['avg'] or 7,
        'ecoli_rate': (
            WaterSample.objects.filter(ecoli_present=True).count() / total_samples * 100
        ) if total_samples > 0 else 0,
        'avg_nitrate': WaterSample.objects.aggregate(avg=Avg('nitrate_level'))['avg'] or 0,
        'avg_risk': WaterSample.objects.aggregate(avg=Avg('risk_score'))['avg'] or 0,
    }

    context = {
        'total_samples': total_samples,
        'high_risk_count': high_risk_count,
        'active_alerts': active_alerts,
        'alerts': alerts,
        'risk_villages': risk_villages,
        'radar_data': radar_data
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
