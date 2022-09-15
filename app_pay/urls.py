from django.urls import path
from .views import ItemView, ItemList, buy_page
from django.views.generic import TemplateView

urlpatterns = [
    path('buy/<int:pk>', buy_page, name='buy_page'),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('item/', ItemList.as_view(), name='item_list'),
    path('', TemplateView.as_view(template_name='main.html'), name='main_page'),
]
