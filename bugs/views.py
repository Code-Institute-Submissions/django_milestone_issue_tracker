from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .models import Bug
from .forms import BugForm

# Create your views here.
def bugs(request):
    """A view that displays the bugs page"""
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    
    
    
@login_required 
def create_bug(request, pk=None):
    """
    Create a view that allows us to create
    a bug
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = BugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bugauthor = request.user.id
            bug.author_id = bugauthor
            bug = form.save()
            return redirect(bugs)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bug_request_form.html', {'form': form})