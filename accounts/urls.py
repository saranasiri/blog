from django.urls import path
from . import views
app_name='accounts'
urlpatterns =[
    path('login/',views.user_login,name='user-login'),
    path('register/',views.user_register,name='user_regiter'),
    path('logout/',views.user_logout,name='user_logout'),
]