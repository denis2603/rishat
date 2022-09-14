from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.views.generic import DetailView
from .models import Item
from .servises import StripeManager


def buy_page(request: HttpRequest, pk: int) -> JsonResponse:
    data = StripeManager().get_session_id(request)
    return JsonResponse(data)


class ItemView(DetailView):

    model = Item
    template_name = 'item.html'
    context_object_name = 'item'
