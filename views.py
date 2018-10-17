from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
def input(request):
    return render(request,'input.html')
def insertt(request):
    pid1=int(request.GET['t1'])
    pname1=request.GET['t2']
    pcost1=float(request.GET['t3'])
    pmfdt1=request.GET['t4']
    pexpdt1=request.GET['t5']
    f=Product(pid=pid1,pname=pname1,pcost=pcost1,pmfdt=pmfdt1,pexpdt=pexpdt1)
    f.save()
    return render(request,'links.html')
def display(request):
    recs=Product.objects.all()
    return render(request,'display.html',{'records':recs})
class ProductList(APIView):
    def get(self,request,format=None):
        products=Product.objects.all()
        serializer=ProductSerializers(products,many=True)
        return Response(serializer.data)
