from django.conf.urls import patterns, include, url

from aggregator import views

urlpatterns = patterns('',
    url(r'^$', views.search, name='search'),
)
