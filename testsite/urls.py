from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'index/$', 'search.views.index'),
    url(r'^search/$', 'search.views.search'),
]
