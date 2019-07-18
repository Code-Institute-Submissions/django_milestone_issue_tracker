from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf


# Create your views here.
def features(request):
    """A view that displays the features page"""
    return render(request, "features.html")

