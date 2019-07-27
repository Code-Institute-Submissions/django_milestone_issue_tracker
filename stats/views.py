from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf
from bugs.models import Bug
from features.models import Feature
from itertools import chain
from django.http import JsonResponse
import json

# Create your views here.
def stats(request):
    """A view that displays the stats page"""
    bugs = Bug.objects.all().count()
    features = Feature.objects.all().count()
    return render(request, "stats.html", {"bugs": bugs, "features": features})

def bug_status_stats(request):
    labels = ["Todo", "In Progress", "Complete"]
    todo = Bug.objects.filter(status='T').count()
    progress = Bug.objects.filter(status="P").count()
    complete = Bug.objects.filter(status="C").count()
    data = {
        'labels': labels,
        'count': [todo, progress, complete],
    }
    return JsonResponse(data)
    
def feature_status_stats(request):
    labels = ["Todo", "In Progress", "Complete"]
    todo = Feature.objects.filter(status='T').count()
    progress = Feature.objects.filter(status="P").count()
    complete = Feature.objects.filter(status="C").count()
    data = {
        'labels': labels,
        'count': [todo, progress, complete],
    }
    return JsonResponse(data)

def bugs_vs_features_stats(request):
    labels = ["Bugs", "Features"]
    bugs = Feature.objects.all().count()
    features = Feature.objects.all().count()
    data = {
        'labels': labels,
        'count': [bugs, features],
    }
    return JsonResponse(data)
    
def top_bugs_stats(request):
    bug_names = []
    bug_upvotes = []
    dataset = list(Bug.objects.values('upvotes', 'name').exclude(
        upvotes=0).order_by('-upvotes')[:3])
    for item in dataset:
        bug_names.append(item['name'])
        bug_upvotes.append(item['upvotes'])

    data = {
        'labels': bug_names,
        'dataset': bug_upvotes
    }
    return JsonResponse(data)
    
def top_feature_stats(request):
    feature_names = []
    feature_upvotes = []
    dataset = list(Feature.objects.values('upvotes', 'name').exclude(
        upvotes=0).order_by('upvotes'))
    for item in dataset:
        feature_names.append(item['name'])
        feature_upvotes.append(item['upvotes'])

    data = {
        'labels': feature_names,
        'dataset': feature_upvotes
    }
    return JsonResponse(data)