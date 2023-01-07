from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    response_string = Hello.objects.all()[0]
    return render(request,'helloworld/index.html',{'data':response_string})


def simple_view(request):
    header = request.META
    ip = header['REMOTE_ADDR']
    html = "<html><head></head><body>HELLOW WITHOUT TEMPLATE"+ip+"</body></html>"  
    return HttpResponse(html,content_type="text/html",status=200)



