from django.shortcuts import render
from main.models import Weather

# Create your views here.
def index(request):
    weathers = [x.digit for x in Weather.objects.all()]
    print(weathers)
    return render(request, 'index.html', {'weather': weathers})
