from django.urls import path, include
from users import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_user),
    path('logout/', views.logout_user),
    path('signup/', views.signup),
]
