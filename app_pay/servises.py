import stripe
from django.urls import reverse
from django.http import HttpRequest
from django.conf import settings


class StripeManager:

    stripe.api_key = settings.SK_STRIPE_KEY

    @staticmethod
    def create_product_and_return_id(id_product: int) -> str:
        product = stripe.Product.create(name=str(id_product))
        return product.id

    @staticmethod
    def create_price_and_return_id(item) -> str:
        price = stripe.Price.create(unit_amount=int(item.price * 100),
                                    currency="usd",
                                    product=item.product_stripe_id,)
        return price.id

    @staticmethod
    def get_session_id(request: HttpRequest, item) -> dict:

        success_url = cancel_url = request.build_absolute_uri(reverse("stub_page"))

        stripe_session = stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancel_url,
            mode='payment',
            line_items=[{"price": item.price_stripe_id, "quantity": 1}],
        )
        data = stripe_session.id
        return data
