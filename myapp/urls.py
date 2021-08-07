from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index  , name='index'),
    url(r'^tower/(?P<id>\d+)$', views.tower  , name='tower'),
    url(r'^tubular/(?P<id>\d+)$', views.tubular  , name='tubular'),

]


admin.site.site_header = 'EPT CEP'
admin.site.index_title = 'EPT CEP'              
admin.site.site_title = 'EPT CEP'

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)