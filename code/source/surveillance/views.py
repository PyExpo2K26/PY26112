import json
import pickle
import os
import pandas as pd
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Village, HealthReport

try:
    with open(os.path.join(settings.BASE_DIR, 'backend', 'model.pkl'), 'rb') as f:
        ml_model = pickle.load(f)
except FileNotFoundError:
    ml_model = None


@csrf_exempt
def sync_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            results = []

            for item in data:
                village, _ = Village.objects.get_or_create(
                    name=item['village_name'],
                    defaults={'latitude': item.get('latitude', 0.0), 'longitude': item.get('longitude', 0.0)}
                )

                # Format features for the ML Model
                features = pd.DataFrame([{
                    'diarrhea_cases': item.get('diarrhea_cases', 0),
                    'vomiting_cases': item.get('vomiting_cases', 0),
                    'fever_cases': item.get('fever_cases', 0),
                    'water_ph': item.get('water_ph', 7.0),
                    'water_turbidity': item.get('water_turbidity', 1.0),
                    'rainfall_mm': item.get('rainfall_mm', 0.0),
                }])

                risk = int(ml_model.predict(features)[0]) if ml_model else 0

                report = HealthReport.objects.create(
                    village=village,
                    diarrhea_cases=item.get('diarrhea_cases', 0),
                    vomiting_cases=item.get('vomiting_cases', 0),
                    water_ph=item.get('water_ph', 7.0),
                    water_turbidity=item.get('water_turbidity', 1.0),
                    risk_score_output=risk
                )
                results.append({"report_id": report.id, "risk": risk, "village": village.name})

            return JsonResponse({"status": "success", "synced_records": len(results), "results": results})
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
    return JsonResponse({"status": "invalid method"}, status=405)


def dashboard_data(request):
    villages = Village.objects.all()
    data = []
    for v in villages:
        latest = HealthReport.objects.filter(village=v).order_by('-timestamp').first()
        if latest:
            data.append({
                "village_id": v.id,
                "name": v.name,
                "lat": v.latitude,
                "lng": v.longitude,
                "diarrhea_cases": latest.diarrhea_cases,
                "vomiting_cases": latest.vomiting_cases,
                "water_ph": latest.water_ph,
                "latest_risk": latest.risk_score_output,
                "last_updated": latest.timestamp.strftime('%Y-%m-%d %H:%M')
            })
    return JsonResponse(data, safe=False)


def dashboard_ui(request):
    from django.shortcuts import render
    return render(request, 'surveillance/dashboard.html')
