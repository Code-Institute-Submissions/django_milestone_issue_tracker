from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Feature
from .forms import FeatureForm



# Create your views here.
def features(request):
    """A view that displays the features page"""
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})

@login_required 
def create_feature(request, pk=None):
    """
    Create a view that allows us to create
    a bug
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            featureauthor = request.user.id
            feature.author_id = featureauthor
            feature = form.save()
            return redirect(features)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'feature_request_form.html', {'form': form})