from django.shortcuts import render

# Create your views here.

def home2(request):
    return render(request,'index.html')

# def sendMessage(request):
#     return render(request,'index.html')