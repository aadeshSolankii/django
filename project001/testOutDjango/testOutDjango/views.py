from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("trying out django - home")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("trying out django - about")

def contact(request):
    return HttpResponse("trying out django - contact")