from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    peoples = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 25},
        {'name': 'Charlie', 'age': 35},
        {'name': 'Diana', 'age': 28},
        {'name': 'Ethan', 'age': 22},
        {'name': 'Fiona', 'age': 27},
        {'name': 'George', 'age': 32},
        {'name': 'Hannah', 'age': 29},
        {'name': 'Ian', 'age': 31},
        {'name': 'Julia', 'age': 26}
        ]
    vegetables = ["Carrot", "Broccoli", "Spinach", "Potato", "Tomato", "Cucumber", "Pepper", "Onion", "Garlic", "Lettuce"]
    return render(request, 'myapp1/index.html' , context = {'peoples': peoples, 'vegetables': vegetables}) 

def secondfiler(request):
    return render(request, 'myapp1/secondfile.html')

def about(request):
    return render(request, 'myapp1/about.html')
def contact(request):
    return render(request, 'myapp1/contact.html')
def base(request):
    return render(request, 'myapp1/base.html')