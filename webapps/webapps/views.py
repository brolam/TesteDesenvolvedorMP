from django.http import HttpResponse

def home(request):
	return HttpResponse("Hello Google AppEngine Django.")