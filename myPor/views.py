from django.shortcuts import render

# Create your views here.
def index(request):
    print("index")
    render(request,'index.html')