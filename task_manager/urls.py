from django.contrib import admin
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('', users_views.SignupUser.as_view(), name='Main'),
    path('admin/', admin.site.urls, name='Admin'),
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
]
