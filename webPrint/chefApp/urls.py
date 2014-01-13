from django.conf.urls import patterns, url

from chefApp import views

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^printFile/(?P<file_id>\d+)/$', views.doPrint, name='printing'),
                       url(r'^printer/(?P<printer_id>\d+)/$', views.printerDetails, name='printerDetails'),
                       url(r'^files/$', views.FileListView.plain_view, name='fileList'),
                       #url(r'^files/(?P<file_id>\d+)/$', ), #for dev only //// insecure
                       url(r'^upload/$', views.upload, name='upload'),

                       #API
                       #url(r'api/', views., name='api_'),
                       url(r'api/files', views.api_file_list, name='api_files'),
                       url(r'api/printers', views.api_printer_list, name='api_printers'),


)
