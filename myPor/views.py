from django.shortcuts import render
from django.http import JsonResponse,HttpResponse

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
