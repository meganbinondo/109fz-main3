# from django.urls import path

# from . import views

# app_name = 'checkout'

# urlpatterns = [
  
#     path('<int:name>/', views.detail, name='checkout'),
#     path('<int:pk>/', views.CheckOut, name='checkout'),
#     path('payment-success/<int:pk>/', views.PaymentSuccessful, name='payment-success'),
#     path('payment-failed/<int:pk>/', views.paymentFailed, name='payment-failed'),
# ]
from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('<int:item_pk>/', views.checkout, name='check'),
    path('purchases/<int:item_pk>/', views.purchases, name='purchases'),
    path('payment-failed/<int:item_pk>/', views.paymentFailed, name='payment-failed'),
    path('payment-success/<int:item_pk>/', views.PaymentSuccessful, name='payment-success'),
    # Add other checkout-related URLs if needed
]
