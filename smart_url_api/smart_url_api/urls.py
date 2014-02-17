from django.conf.urls import patterns, include, url

from django.contrib import admin
from url_short_api.api import ShorteningResource,StatsResource
from smart_shortener_fe import views
from tastypie.api import Api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

v1_api = Api()
v1_api.register(ShorteningResource())
v1_api.register(StatsResource())
urlpatterns = patterns('',
                       
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/',include(v1_api.urls)),
    url(r'smart_fe$',views.index,name="index"),
    url(r'^smart_fe/(?P<short_hash>\w+)/$', views.redirect_user_to_page),
) 

urlpatterns += staticfiles_urlpatterns()
