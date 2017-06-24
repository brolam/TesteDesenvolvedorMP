from django.conf.urls import include, url

urlpatterns = [url(r'^$', 'webapps.views.home', name='home'),]