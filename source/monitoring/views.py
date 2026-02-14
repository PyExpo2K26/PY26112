from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Count, Q
from .models import WaterSample, Alert
from .forms import WaterSampleForm

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

@login_required
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

    context = {
        'total_samples': total_samples,
        'high_risk_count': high_risk_count,
        'active_alerts': active_alerts,
        'alerts': alerts,
        'risk_villages': risk_villages
    }
    return render(request, 'monitoring/dashboard.html', context)

@login_required
def submit_sample(request):
    if request.method == 'POST':
        form = WaterSampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.user = request.user
            sample.save()
            return redirect('dashboard')
    else:
        form = WaterSampleForm()
    return render(request, 'monitoring/submit_sample.html', {'form': form})

@login_required
def alert_list(request):
    alerts = Alert.objects.all().order_by('-created_at')
    return render(request, 'monitoring/alerts.html', {'alerts': alerts})
