from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.template.context_processors import csrf


# Create your views here.
def cart(request):
    """A view that displays the cart page"""
    return render(request, "cart.html")

