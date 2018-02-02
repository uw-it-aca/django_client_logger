from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('django_client_logger.urls')),
]
