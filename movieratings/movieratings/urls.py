from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^movielens/', include('movielens.urls')),
    url(r'^admin/', admin.site.urls),
]
