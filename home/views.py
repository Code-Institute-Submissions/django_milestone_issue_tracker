from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature


def index(request):
    """A view that displays the index page"""
    bugs = Bug.objects.order_by('-upvotes')[:5]
    features = Feature.objects.order_by('-upvotes')[:5]
    args = {
        "bugs": bugs,
        "features": features,
    }
    return render(request, "index.html", args)
