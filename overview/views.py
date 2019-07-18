from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf


# Create your views here.
def overview(request):
    """A view that displays the overview page"""
    return render(request, "overview.html")

