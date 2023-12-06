# users/forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from .models import UserProfile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'fullname', 'address', 'phone_number', 'update_password']

    fullname = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Your full name',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Your address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    phone_number = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Your phone number',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    edit_password = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-check-input',
    }))

    new_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'placeholder': 'New password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    confirm_new_password = forms.CharField(required=False, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm new password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def clean(self):
        cleaned_data = super().clean()
        edit_password = cleaned_data.get("edit_password")
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if edit_password and (not new_password or not confirm_new_password):
            raise forms.ValidationError("Please provide both new password and confirmation.")
        
        if new_password != confirm_new_password:
            raise forms.ValidationError("New password and confirmation do not match.")

        return cleaned_data
