from django.shortcuts import render

# Create your views here.
def realme(request):
    return render(request, "realme.html")

def samsung(request):
    return render(request, "samsung.html")