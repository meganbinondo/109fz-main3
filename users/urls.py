# users/urls.py
# users/urls.py
from django.urls import path
from .views import view_profile, update_profile

app_name = 'users'

urlpatterns = [
    path('view_profile/', view_profile, name='view_profile'),  # Make sure to define the name parameter
    path('update_profile/', update_profile, name='update_profile'),
    # other URLs
]
