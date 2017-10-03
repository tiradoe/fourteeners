from django.conf.urls import patterns, url
from apps.mountains import views

urlpatterns = patterns('',
    url(r'^$', views.list, name='list'),
    url(r'^edit/(?P<peak>\d+)/$', views.edit, name='edit'),
    url(r'^new/(?P<peak>\d+)/$', views.new, name='new'),
    url(r'^delete/(?P<climb>\d+)/$', views.ClimbDelete.as_view(), name='delete_climb'),
    url(r'^weather/(?P<peak>\d+)/$', views.weather, name='weather'),
)
