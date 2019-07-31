from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature
from itertools import chain


def overview(request):
    """A view that displays the overview page"""
    bugs = Bug.objects.all()
    features = Feature.objects.all()
    results = sorted(chain(bugs, features), key=lambda result: result.upvotes,
                     reverse=True)
    return render(request, "overview.html", {"results": results})
