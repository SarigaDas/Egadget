from django.urls import path
from account.views import *


urlpatterns = [
    path('reg',RegView.as_view(),name='reg'),
    path('logout',LgoutView.as_view(),name='logout')
]