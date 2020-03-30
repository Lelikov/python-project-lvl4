from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.LoginUser.as_view(), name='SignIn'),
    url(r'^logout/$', views.LogoutUser.as_view(), name='LogOut'),
    url(r'^signup/$', views.SignupUser.as_view(), name='SignUp'),
]
