from django.shortcuts import render
from django.db.models import Q
from features.models import Feature

# Create your views here.
def do_search_features(request):
    features = Feature.objects.filter(Q(name__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, "features.html", {"features": features})