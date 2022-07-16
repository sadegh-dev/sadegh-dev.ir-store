from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('secret :) /', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('odrers/', include('orders.urls', namespace='orders')),
    path('api/', include('doapi.urls', namespace='doapi')),
    path('api-token-auth/',obtain_auth_token, name='mytoken'),
    path('', include('doshop.urls', namespace='doshop')),

] 
# + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)  
