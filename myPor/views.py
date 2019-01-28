from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json

# Create your views here.
def index(request):
    print("index")
    return render(request,'index.html')
def search(request):
    return render(request,'work.html')

def returnR(request):
    if("POST" == request.method):
        print("request is post")
        datas = request.POST['val']
        print("received data:"+datas)
        r="hello word!"
        return HttpResponse(r)
def login(request):
    return render(request,"Login.html")

def submit(request):
    if('POST'==request.method):
        print("submit_request is post")
        datas=json.loads(request.POST['userinfo'])
        print(datas)
        if(datas['username']=="admin" and datas['password']=="123456"):
            content={"message":"success"}
        else:
            content={"message":"fail"}
    else:
        content={"message":"fail"}
    return JsonResponse(content)
def component(request):
    return render(request,"component.html")


