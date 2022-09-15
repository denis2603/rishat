
from django.http import HttpRequest, JsonResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404
from .models import Item
from .servises import StripeManager


def buy_page(request: HttpRequest, pk: int) -> JsonResponse:
    item = get_object_or_404(Item, pk=pk)
    session_id = StripeManager().get_session_id(request, item)
    return JsonResponse({'id': session_id})


class ItemView(DetailView):

    model = Item
    template_name = 'item.html'
    context_object_name = 'item'


class ItemList(ListView):

    model = Item
    template_name = 'item_list.html'
    context_object_name = 'item_list'
