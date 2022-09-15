import stripe
from django.shortcuts import render, redirect
from .models import Item, ItemAPI
from django.views import View
from django.conf import settings
from django.http import JsonResponse


def index(request):
    goods = Item.objects.all()
    data = {
        'goods': goods,
    }
    return render(request, 'index.html', context=data)


def CreateCheckoutSessionView(request, *args, **kwargs):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    YOUR_DOMAIN = 'http://127.0.0.1:8000'
    pk = kwargs.get('pk', None)
    good_item_id = ItemAPI.objects.get(pk=pk)
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                "price": good_item_id.api_id,
                "quantity": 1,
            },
        ],
        currency='usd',
        mode='payment',
        success_url=YOUR_DOMAIN + '/success',
        cancel_url=YOUR_DOMAIN + '/cancel',
    )
    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def goods_info(request, *args, **kwargs):
    pk = kwargs.get('pk', None)
    item = Item.objects.get(pk=pk)
    data = {
        'good': item
    }
    return render(request, 'ptoduct_page.html', context=data)