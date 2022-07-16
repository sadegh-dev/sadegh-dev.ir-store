
from django.urls import path
from . import views


app_name = 'orders'

urlpatterns = [
    path('create/',views.order_create, name='order_create'), 
    path('order-detail/<int:order_id>/',views.order_detail, name='order_detail'), 
    path('order-delete/<int:order_id>/',views.order_delete, name='order_delete'), 
    path('orders-list/',views.order_list, name='order_list'), 
]
