from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def index(request):
    response_string = Hello.objects.all()[0]
    return render(request,'helloworld/index.html',{'data':response_string})


def simple_view(request):
    #header = request.META
    #ip = header['REMOTE_ADDR']
    addressess = Address.object.all()
    first_address = addressess[0]
    resident_name = str(first_address.resident)
    #html = "<html><head></head><body>HELLOW WITHOUT TEMPLATE   Name:"+resident_name+"<br/> Address:"+first_address+"</body></html>"  
    #return HttpResponse(html,content_type="text/html",status=200)
    #return HttpResponse(html)
    return render(request, 'helloworld/simple.html', {'address':first_address, 'name':resident_name} )

