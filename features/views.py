from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from .models import Feature, UpvoteFeature, CommentFeature
from .forms import FeatureForm, FeatureCommentForm



# Create your views here.
def features(request):
    """A view that displays the features page"""
    features = Feature.objects.all()
    return render(request, "features.html", {"features": features})

def feature_detail(request, pk):
    """
    Create a view that returns a single
    Feature object based on the post ID (pk) and
    render it to the 'feature_detail.html' template.
    Or return a 404 error if the feature is
    not found
    """
    feature = get_object_or_404(Feature, pk=pk)
    feature.views += 1
    feature.save()
    comments = CommentFeature.objects.filter(feature=feature).order_by('-created_date')
    if request.method == 'POST':
        comment_form = FeatureCommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            comment = CommentFeature.objects.create(feature=feature, comment_author=request.user, content=content)
            comment.save()
    else:
        comment_form = FeatureCommentForm()

    args = {
        'feature': feature,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, "feature_detail.html", args)

@login_required 
def create_feature(request, pk=None):
    """
    Create a view that allows us to create
    a feature
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = FeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            featureauthor = request.user.id
            feature.author_id = featureauthor
            feature = form.save()
            return redirect(features)
    else:
        form = FeatureForm(instance=feature)
    return render(request, 'feature_request_form.html', {'form': form})
    
@login_required
def upvote_feature(request, pk):
    feature = Feature.objects.get(pk=pk)
    user_voted_id = request.user.id
    upvote = UpvoteFeature.objects.filter(feature=feature, user_voted_id=user_voted_id)
    
    if not upvote:
        upvote = UpvoteFeature(feature=feature, user_voted_id=request.user.id)
        upvote.save()
        feature.vote_price = 5.00
        feature.save()
        cart = request.session.get('cart', {})
        id = feature.pk
        cart[id] = cart.get(id, 1)
        request.session['cart'] = cart
        messages.success(request, 'Upvote added to cart', extra_tags="alert-success")
        return redirect(feature_detail, feature.pk)
    else:
        messages.error(request, 'You need to pay for your vote!', extra_tags="alert-danger")
        return redirect(feature_detail, feature.pk)