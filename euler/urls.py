from django.conf.urls import url
from django.contrib import admin
from web.views import search


urlpatterns = [
    url(r'^$', search),
    url(r'^admin/', admin.site.urls),
]
