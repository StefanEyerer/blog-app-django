from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic.base import RedirectView
from . import views as user_views

app_name = 'users'
urlpatterns = [
    path('', RedirectView.as_view(url='profile'), name='index'),
    path('profile/', user_views.profile, name='profile'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/user_login.html',
         redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/user_logout.html'), name='logout'),
]
