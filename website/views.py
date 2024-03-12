from django.shortcuts import render,HttpResponse
from .models import property, blog, agent, images
from django.db.models import Q

# Create your views here.
def home(request):
    sell = property.objects.all().filter(stat='2')
    data = blog.objects.all().filter(STATUS='2')    
    return render (request,'index.html',{'sell':sell,'post':data})
def buy(request):
    buy = property.objects.all().filter(stat ='2')
    return render(request,'buy.html',{'data':buy})
def sell(request):
    return render(request,'sell.html',{'data':buy})

def rent(request):
    return render(request,'rent.html')
def blogs(request):
    return render (request,'blog.html')
def about(request):
    return render (request,'about.html')
def contact(request):
    return render (request,'contact.html')
def search(request):
    if request.method == 'GET':
        term = request.GET.get('term')
    data = property.objects.filter(Q(address__contains=term))
    return render(request,'search.html',{'data':data ,'terms': term})

def listing(request,id):
    data = property.objects.get(pk=id)
    image = images.objects.filter(listing=data.id)
    keyname = (data.agent)
    agentData = agent.objects.get(name=keyname)
    
    return render(request,'listing.html',{'data':data,'data1':agentData,'images':image})