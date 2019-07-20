from django.shortcuts import render
from features.models import Feature

# Create your views here.
def do_search_features(request):
    features = Feature.objects.filter(name__icontains=request.GET['q'])
    return render(request, "features.html", {"features": features})