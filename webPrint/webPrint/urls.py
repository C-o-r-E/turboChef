from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'^$', 'webPrint.views.home', name='home'),
                       url(r'^print/', include('chefApp.urls')),
                       url(r'^admin/', include(admin.site.urls)),
) +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
