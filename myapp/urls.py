from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.landing  , name='landing'),
    url(r'farm', views.home  , name='index'),
    
    url(r'booked', views.booked  , name='booked'),
    url(r'checked', views.checked  , name='checked'),
    url(r'contacted', views.contacted  , name='contacted'),
    url(r'landing', views.landing  , name='landing'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)