from django.conf.urls import url
from tasks import views

urlpatterns = [
    url(r'^$', views.TasksViews.as_view(), name='TaskViews'),
    url(r'^create/$', views.TaskCreate.as_view(), name='TaskCreate'),
    url(r'^(?P<pk>\d+)/delete/$', views.DeleteTask.as_view(),
        name='TaskDelete'),
    url(r'^(?P<pk>\d+)/edit/$', views.TaskEdit.as_view(), name='TaskEdit'),

    url(r'^status/create/$', views.StatusCreate.as_view(),
        name='StatusCreate'),
    url(r'^status/$', views.StatusViews.as_view(), name='StatusViews'),
    url(r'^status/(?P<pk>\d+)/edit/$', views.StatusEdit.as_view(),
        name='StatusEdit'),
    url(r'^status/(?P<pk>\d+)/delete/$', views.StatusDelete.as_view(),
        name='StatusDelete'),

    url(r'^tag/create/$', views.TagCreate.as_view(), name='TagCreate'),
    url(r'^tag/$', views.TagViews.as_view(), name='TagViews'),
    url(r'^tag/(?P<pk>\d+)/edit/$', views.TagEdit.as_view(), name='TagEdit'),
    url(r'^tag/(?P<pk>\d+)/delete/$', views.TagDelete.as_view(),
        name='TagDelete'),
]
