from django.conf.urls import patterns, url

from chefApp import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^printer/(?P<printer_id>\d+)/$', views.printerDetails, name='printerDetails'),
)
