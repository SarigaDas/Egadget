from django.urls import path
from .views import *

urlpatterns = [
    path('custhome',CustomerHomeView.as_view(),name='custhome'),
    path('pdetail/<int:id>',ProductDetailView.as_view(),name='pdet'),
    path('acart/<int:id>',addcart,name="acart"),
    path('cartlist',CartListView.as_view(),name="clist"),
    path('rcart/<int:id>',removecart,name="rcart"),
    path('pymnt/<int:id>',PaymentView.as_view(),name="pay"),
    path('order',OrderListView.as_view(),name="myorders"),
    path('cancelorders/<int:id>',cancelorder,name='cancelorder')

]