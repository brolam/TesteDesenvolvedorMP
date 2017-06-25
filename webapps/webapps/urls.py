from django.conf.urls import include, url

urlpatterns = [ 
				url(r'^$', 'webapps.views.home', name='home'), 
				url(r'', include('candidates.urls', namespace="candidates" )),
			]