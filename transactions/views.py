# views.py
# from item.models import Item
# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from .models import Purchase

# @login_required
# def user_purchases(request):
#     # Retrieve user purchases from the database and order them by transaction date
#     purchases = Purchase.objects.filter(user=request.user).order_by('-transaction_date')
    
#    

#     context = {
#         'purchases': purchases,
#         'shipping' : shipping_fee,
#         'price' : price
#     }

#     return render(request, 'user_purchases.html', context)

# views.py

# from django.shortcuts import render, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Purchase
# from item.models import Item
# from decimal import Decimal

# @login_required
# def user_purchases(request):
    
#     purchases = Purchase.objects.filter(user=request.user).order_by('-transaction_date')

#     if request.method == 'POST':
      
#         # Create a new Purchase instance
#         purchase = Purchase.objects.create(
#             user=request.user,
#             item=item,
#             transaction_date=timezone.now()
#         )

#         # Redirect to a success page or do whatever you need
#         # return redirect('success_page')

#     context = {
#         'item': item
#     }

#     return render(request, 'user_purchases.html', context)

# views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Purchase

@login_required
def user_purchases(request):
    # Retrieve user purchases from the database and order them by transaction date
    purchases = Purchase.objects.filter(user=request.user).order_by('-transaction_date')

    context = {
        'purchases': purchases
    }

    return render(request, 'user_purchases.html', context)

