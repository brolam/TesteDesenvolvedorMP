from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def home(request):
	return HttpResponseRedirect(reverse('candidates:evaluation_new'))