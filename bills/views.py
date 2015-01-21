from django.shortcuts import render
from django.http import HttpResponse
from bills.models import *

# Create your views here.

def bil_index(request):
    return render(request, 'main.html')

def bill(request):
    car = Choice.objects.get('carat')
    form = bill_form() 
    for i in Choice:
       
        if (car == 23):
            cost = 0.96*(rate_of_pure)*weight
        elif (car == 22):
            cost = 0.92*(rate_of_pure)*weight
        elif (car == 18):
            cost = 0.75*rate_of_pure*weight
        elif (car == 14):
            cost = 0.6*rate_of_pure*weight
        else: 
            print invalid
         
    Choice.objects.all().aggregate(Sum('cost'))

    return render(request, 'bill.html',{'form':bill_form}) 
