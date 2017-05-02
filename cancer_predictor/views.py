from django.shortcuts import render

from django.http import HttpResponse

from .forms import RegistrationForm

from .BreastCancer import pred

def index(request):
    form = RegistrationForm()

    context = {
        "myregistrationform":form
    }
    return render(request, 'cancer_predictor/cancer_predictor.html', context)

def prediction(request):

    val = pred(request.POST)
    if(val == 2):
        ans = "Benign"
        message = "Congratualtions! Your cancer cells are benign."
    else:
        ans = "Malignant"
        message = "We are sorry, unfortunately your cancer cells are malignant. We suggest you visit a doctor as soon as possible for further check up."
    context = {
        "result":ans,
        "message":message
    }
    return render(request, 'cancer_predictor/result.html', context)
