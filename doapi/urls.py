from django.urls import path
from . import views


app_name = 'doapi'
urlpatterns = [
    path('test-connect/',views.test_connect),
    path('test-post-get/',views.test_post_get),  
    path('all-categories/',views.categories), 
    path('all-companies/',views.companies), 
    path('special-price-products/',views.special_price_products), 
    path('category-products/<slug:slug>/',views.category_products),
    path('get-token/', views.get_token, name='get_token'),
    path('my-orders/', views.my_orders, name='my_orders'),

]
