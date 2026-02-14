from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignupForm

def home(request):
    import json
    from .models import DiseaseInfo
    diseases = DiseaseInfo.objects.all()
    
    # Process bio_profiles for template display
    for disease in diseases:
        try:
            raw_bio = json.loads(disease.bio_profile) if disease.bio_profile else {}
            # Format keys for clean display in template
            disease.parsed_bio = {k.replace('_', ' '): v for k, v in raw_bio.items()}
        except:
            disease.parsed_bio = {}
            
    disease_count = diseases.count()
    return render(request, 'web/home.html', {
        'disease_count': disease_count,
        'diseases': diseases
    })


def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('home')
	else:
		form = SignupForm()

	return render(request, 'web/signup.html', {'form': form})

def predict_water_quality(request):
    prediction = None
    remedy = None
    bio_info = None
    if request.method == 'POST':
        try:
            data = {
                'Water_Color': request.POST.get('Water_Color'),
                'Water_Odor': request.POST.get('Water_Odor'),
                'Water_Source': request.POST.get('Water_Source', 'Tap'),
            }
            # Import here to avoid circular imports or loading issues at startup if libs missing
            from .utils import make_prediction
            prediction, remedy, bio_info = make_prediction(data)

            # Save prediction if user is logged in
            if request.user.is_authenticated and not prediction.startswith("Error"):
                from .models import UserPrediction
                UserPrediction.objects.create(
                    user=request.user,
                    symptom_text="", # No longer collected
                    water_color=data['Water_Color'],
                    water_odor=data['Water_Odor'],
                    prediction=prediction,
                    remedy=remedy
                )

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'web/predict.html', {
        'prediction': prediction, 
        'remedy': remedy,
        'bio_info': bio_info
    })
