from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf
from bugs.models import Bug
from features.models import Feature
from itertools import chain

# Create your views here.
def overview(request):
    """A view that displays the overview page"""
    bugs = Bug.objects.all()
    features = Feature.objects.all()
    results = sorted(chain(bugs, features), key=lambda result: result.upvotes, reverse=True)
    return render(request, "overview.html", {"results": results})

