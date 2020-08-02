from django.shortcuts import render, get_object_or_404
from services.models import Training_Type
from .forms import PurchaseOrderForm
from django.conf import settings

import stripe
# Create your views here.


def checkout(request, article_name):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_PUBLIC_KEY

    article_name = get_object_or_404(Training_Type, name=article_name)
    purchase_amount = round(article_name.price * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=purchase_amount,
        currenct=settings.STRIPE_CURRENCY,
    )
    print(intent)

    purchase_order_form = PurchaseOrderForm()
    context = {
       'purchase_order_form': purchase_order_form,
       'article_name': article_name,
       'client_secret': 'test',
       'stripe_public_key': 'pk_test_51HBh7BBZlYFkG3UBGr91WrMsmK9On6r6U3XUrzeJErc9UqButB5248Y3MLppdPdDkDXolV3tAnRVG0TtUEQTIpIu00sm7Rid2L'
    }
    return render(request, "checkout/index.html", context)
