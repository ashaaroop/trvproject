from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import place
from .models import team

# Create your views here.
def demofn(request):
     obj=place.objects.all()
     obj1 = team.objects.all()
     return render(request,"index.html",{'result':obj,'item':obj1})


# def addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      return render(request,"about.html",{'result':res})