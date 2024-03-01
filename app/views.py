from django.shortcuts import render

# Create your views here.

def boot_strap(request):
    return render(request,'boot_strap.html')