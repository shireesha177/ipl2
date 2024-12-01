from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def captain(request):
    return HttpResponse('<h1>RUTURAJ is captain of CSK</h1>')
def vicecaptain(request):
    return HttpResponse('<h1>JADIJA is vicecaptain of CSK</h1>')   

