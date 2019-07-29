from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf
from bugs.models import Bug
from features.models import Feature
from itertools import chain
from django.db.models import Q

def do_search_overview(request):
    bugs = Bug.objects.filter(Q(name__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    features = Feature.objects.filter(Q(name__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    results = sorted(chain(bugs, features), key=lambda result: result.upvotes, reverse=True)
    return render(request, "overview.html", {"results": results})
