from __future__ import unicode_literals

from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^admin/', include(admin.site.urls))

]
