from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('ems_wheniwork.urls')),
]
