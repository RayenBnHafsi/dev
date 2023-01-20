from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='App_manage.home'),
    path('product', views.product, name='App_manage.product'),
    path('slider', views.slider, name='App_manage.slider'),
]