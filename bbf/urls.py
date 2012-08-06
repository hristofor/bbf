from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from models import *
from views import *
from bbf import views

urlpatterns = patterns('',
    url(r'^$', 'bbf.views.home'),
    url(r'^file/$', views.file),
    url(r'^team/$', views.team),
    url(r'^hall/$', views.hall),
    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    url(r'^file/(?P<id>\d+)/$', views.player_info),
    url(r'^teams/(?P<id>\d+)/$', views.team_info),
)
