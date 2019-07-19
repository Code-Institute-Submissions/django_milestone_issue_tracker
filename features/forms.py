from django import forms
from .models import Feature, CommentFeature


class FeatureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('name', 'description')
        
class FeatureCommentForm(forms.ModelForm):
    class Meta:
        model = CommentFeature
        fields = ('content',)