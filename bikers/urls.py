from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'parkingApp.views.index', name='index'),
	#for testing!!
	#url(r'^getMarkers/$', 'parkingApp.views.getMarkers', name='markers'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('allauth.urls')),
	] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # change for production!