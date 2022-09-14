from django.urls import path
from .views import ItemView, buy_page
from django.http import HttpResponse

urlpatterns = [
    path('buy/<int:pk>/', buy_page, name='buy_page'),
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('', lambda _: HttpResponse('Stab page'), name='stub_page'),
]
