from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.submit_sample, name='submit_sample'),
    path('alerts/', views.alert_list, name='alert_list'),
    path('alerts/<int:alert_id>/resolve/', views.resolve_alert, name='resolve_alert'),
    path('send-sms/<int:sample_id>/', views.send_sms, name='send_sms'),
    
    # Nearby Water Sources (IP Geolocation + GPS)
    path('nearby/', views.nearby_sources, name='nearby_sources'),
    path('nearby/api/', views.nearby_sources_api, name='nearby_sources_api'),

    # HACKATHON PIVOT: Offline SMS & Smart Dispatch Features
    path('twilio-webhook/', views.twilio_webhook, name='twilio_webhook'),
    path('smart-dispatch/', views.smart_dispatch, name='smart_dispatch'),
    path('smart-dispatch/<int:alert_id>/dispatch/', views.dispatch_van, name='dispatch_van'),
    path('smart-dispatch/<int:alert_id>/resolve/', views.resolve_dispatch, name='resolve_dispatch'),
]

