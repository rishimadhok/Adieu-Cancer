from django.shortcuts import render

from django.http import HttpResponse
 
def index(request):
    return render(request, 'cancerA_Z/cancerA_Z.html', {})
