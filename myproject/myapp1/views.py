from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    return render(request, 'myapp1/index.html')

def secondfiler(request):
    return render(request, 'myapp1/secondfile.html')