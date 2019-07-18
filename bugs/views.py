from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf


# Create your views here.
def bugs(request):
    """A view that displays the bugs page"""
    return render(request, "bugs.html")

