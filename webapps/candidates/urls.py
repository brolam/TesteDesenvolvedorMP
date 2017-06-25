from django.conf.urls import url

urlpatterns = [
	url(r'^candidates/evaluation/new$', 'candidates.views.evaluation_new', name='evaluation_new'),
	]