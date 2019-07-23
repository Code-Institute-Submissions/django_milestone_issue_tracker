from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('full_name', 'phone', 'address1', 'address2', 'postcode', 
        'town', 'county', 'country')
