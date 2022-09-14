import stripe
from django.urls import reverse
from django.http import HttpRequest


class StripeManager:

    stripe.api_key = 'sk_test_51Lhx3GECEwsf2aEWqGvwkXW3r1ZstDdxsCQj3FxfU7Z3slmWhFurT94LqBHaaX4EroDGiRuB6P83qvUfdGUrgHIy00CnU81PHa'

    @staticmethod
    def create_and_return_id_stripe_product(id_product: int) -> str:
        product = stripe.Product.create(name=str(id_product))
        return product.id

    @staticmethod
    def get_session_id(request: HttpRequest) -> dict:

        success_url = cancel_url = request.build_absolute_uri(reverse("stub_page"))

        stripe_session = stripe.checkout.Session.create(
            success_url=success_url,
            cancel_url=cancel_url,
            mode='payment',
            line_items=[{"price": 'price_1LhxbUECEwsf2aEWW4xVYjrP', "quantity": 2}],
        )

        data = stripe_session

        return data
