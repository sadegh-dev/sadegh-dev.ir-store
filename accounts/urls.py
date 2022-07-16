from django.urls import path
from . import views
 
app_name = 'accounts'
urlpatterns = [
    path('register/',views.user_register, name='user_register'),
    path('login/',views.user_login, name='user_login'),
    path('logout/',views.user_logout, name='user_logout'),
    path('user-edit/', views.user_edit, name="user_edit"),
    path('profile/', views.user_profile, name='user_profile'),
    path('list-api/', views.list_api, name='list_api'),
    path('user-change-pass/', views.user_change_pass, name='user_change_pass'),
    #reset password
    path('reset/', views.UserPassReset.as_view(), name='reset_pass'),
	path('reset/done/', views.UserPassResetDone.as_view(), name='reset_pass_done'),
	path('reset/<uidb64>/<token>', views.UserPassResetConfirm.as_view(), name='reset_pass_confirm'),
	path('reset/complete/', views.UserPassResetComplete.as_view(), name='reset_pass_complete'),
]
