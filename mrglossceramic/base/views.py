from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request ,'base/home.html')

def franchise_page(request):
    return render(request, "base/franchise.html")
