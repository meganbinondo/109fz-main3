# urls.py

from django.urls import path
from .views import user_purchases


app_name = 'transactions'

urlpatterns = [
    # ... other URL patterns ...
    path('transactions/', user_purchases, name='user_purchases'),
]
