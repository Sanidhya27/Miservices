from django.shortcuts import render
from forms import ServiceRequest
from .models import Product,ProductRequest
# Create your views here.
def display(request):
	if request.method=='POST':
		p=Product.objects.get(name=request.POST['QuantityName'])
		print(p)
		obj=ProductRequest.objects.create(quantityname=p,Department=request.POST['Demandedby'],quantitydemanded=request.POST['QuantityDemanded'],quantitysupplied=request.POST['QuantitySupplied'])
		obj.save()
		form=ServiceRequest(request.POST)
		return render(request,'Product/ok.html',{'form':form})
	if request.method=='GET':
		form=ServiceRequest(request.POST)
		return render(request,'Product/ok.html',{'form':form})
def index(request):
	if request.method=='GET':
		form=ServiceRequest(request.GET)
		print(form)
		
	return render(request,'Product/index.html',{'form':form})		