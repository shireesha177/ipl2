from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def captain(request):
    return HttpResponse('<h1>HARDIK PANDYA is captain of MI</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>ROHIT is vicecaptain of MI</h1>')   

