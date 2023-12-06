# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import UpdateProfileForm
from .models import UserProfile

@login_required
def view_profile(request):
    # user_profile = request.user.userprofile
    
    try:
        user_profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        user_profile = None

    return render(request, 'view_profile.html', {'user_profile': user_profile})

@login_required
def update_profile(request):
    # Check if the user has a UserProfile; create one if not.
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, request.FILES, instance=user_profile)

        if form.is_valid():
            form.save()

            if form.cleaned_data.get('edit_password'):
                new_password = form.cleaned_data.get('new_password')
                confirm_new_password = form.cleaned_data.get('confirm_new_password')

                if new_password and new_password == confirm_new_password:
                    request.user.set_password(new_password)
                    request.user.save()
                    messages.success(request, 'Password updated successfully.')
                else:
                    messages.error(request, 'Passwords do not match.')

            messages.success(request, 'Profile updated successfully.')
            
            storage = messages.get_messages(request)
            storage.used = True

            return redirect('users:view_profile')
    else:
        form = UpdateProfileForm(instance=user_profile)

    return render(request, 'update_profile.html', {'form': form})

