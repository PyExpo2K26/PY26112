from django.contrib import admin
from django.urls import path, include
from surveillance import views as surveillance_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monitoring.urls')),
    path('api/sync/', surveillance_views.sync_data),
    path('api/dashboard/', surveillance_views.dashboard_data),
    path('surveillance/', surveillance_views.dashboard_ui),
]
