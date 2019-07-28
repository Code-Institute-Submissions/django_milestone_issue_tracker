from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .models import Bug, UpvoteBug, CommentBug
from .forms import BugForm, BugCommentForm

# Create your views here.
def bugs(request):
    """A view that displays the bugs page"""
    bugs = Bug.objects.all()
    return render(request, "bugs.html", {"bugs": bugs})
    
def bug_detail(request, pk):
    """
    Create a view that returns a single
    Bug object based on the post ID (pk) and
    render it to the 'bug_detail.html' template.
    Or return a 404 error if the bug is
    not found
    """
    bug = get_object_or_404(Bug, pk=pk)
    bug.views += 1
    bug.save()
    comments = CommentBug.objects.filter(bug=bug).order_by('-created_date')
    if request.method == 'POST':
        comment_form = BugCommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment = CommentBug.objects.create(bug=bug, comment_author=request.user, content=content)
            comment.save()
            messages.success(request, "You have successfully posted a comment")
    else:
        comment_form = BugCommentForm()

    args = {
        'bug': bug,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, "bug_detail.html", args)
    
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
            bug.created_date = timezone.now()
            bug = form.save()
            return redirect(bugs)
    else:
        form = BugForm(instance=bug)
    return render(request, 'bug_request_form.html', {'form': form})
    
@login_required
def upvote_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    user_voted_id = request.user.id
    upvote = UpvoteBug.objects.filter(upvoted_bug=bug, user_voted_id=user_voted_id)
    
    if not upvote:
        upvote = UpvoteBug(upvoted_bug=bug, user_voted_id=request.user.id)
        upvote.save()
        bug.upvotes += 1
        bug.save()
        messages.success(request, "Thanks for your vote!")
        return redirect(bug_detail, bug.pk)
    else:
        messages.error(request, 'You have already voted for this!', extra_tags="alert-danger")
        return redirect(bug_detail, bug.pk)