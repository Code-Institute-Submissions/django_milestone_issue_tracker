from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf


# Create your views here.
def checkout(request):
    """A view that displays the checkout page"""
    return render(request, "checkout.html")

