# Create your views here.
import uuid
from item.models import Item
from django.urls import reverse
from django.conf import settings
from transactions.models import Purchase 
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render, get_object_or_404


def checkout(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    host = request.get_host()
    # Add your checkout logic here

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': item.price,
        'item_name': item.name,
        'invoice': uuid.uuid4(),
        'currency_code': 'PHP',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('checkout:payment-success', kwargs = {'item_pk': item.id})}",
        'cancel_url': f"http://{host}{reverse('checkout:payment-failed', kwargs = {'item_pk': item.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'item': item,   
        'paypal': paypal_payment

    }

    return render(request, 'checkout.html', context)


# Create your views here.

# def CheckOut(request, item_pk):

#     item = get_object_or_404(Item, pk=item_pk)

#     context = {
#         'item': item,
        
#     }

#     return render(request, 'checkout.html', context)


def PaymentSuccessful(request, item_pk):

    item = get_object_or_404(Item, pk=item_pk)

    return render(request, 'payment-success.html', {'item': item})

def paymentFailed(request, item_pk):

    item = get_object_or_404(Item, pk=item_pk)

    return render(request, 'payment-failed.html', {'item': item})

def purchases(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    quantity = int(request.POST.get('quantity', 1))
    address = request.POST.get('address', '')
    region = request.POST.get('region', '')

    # Define shipping fees based on the region
    shipping_fees = {'Luzon': 150, 'Visayas': 100, 'Mindanao': 50}

    # Get the shipping fee based on the selected region
    shipping_fee = shipping_fees.get(region, 0)

    # Calculate the total amount including the shipping fee
    total_amount = (item.price * quantity) + shipping_fee
    
    purchase = Purchase.objects.create(
        user=request.user,
        item=item,
        total_amount=total_amount,
        # Add other fields as needed
    )

    context = {
        'item': item,
        'quantity': quantity,
        'address': address,
        'region': region,
        'shipping_fee': shipping_fee,
        'total': total_amount
    }

    return render(request, 'purchases.html', context)

