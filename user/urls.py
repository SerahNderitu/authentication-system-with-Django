
from django.urls import path
from . import views
from user import views as user_view
from django.contrib.auth import views as auth


urlpatterns = [
    path('', views.index, name='index'),
    path('register/', user_view.register, name='register'),
    path('login/', user_view.user_login, name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='user/index.html'), name='logout'),
]
