from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
    
@login_required 
def profile(request):
    user_profile = UserProfile.objects.all()
    return render(request, "profile.html", {"user_profile": user_profile})

@login_required
def update_profile(request, pk=None):
    """A view that manages the profile form"""
    user_profile = get_object_or_404(UserProfile, pk=pk) if pk else None
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            userauthor = request.user.id
            user_profile.user_id = userauthor
            user_profile = form.save()
            messages.error(request, "Details successfully updated!")
            return redirect(profile)
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'profile_form.html', {'form': form})
