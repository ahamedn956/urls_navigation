from django.shortcuts import render

# Create your views here.

def seats(request):
    return render(request,'seats.html')