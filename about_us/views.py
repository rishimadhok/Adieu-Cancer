from django.shortcuts import render

# Create your views here.

#def index(request):
#	return render(request, 'about_us/about_us.html', {})


from django.http import HttpResponse
 
def index(request):
    return render(request, 'about_us/about_us.html', {})
