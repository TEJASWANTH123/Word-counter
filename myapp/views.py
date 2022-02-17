from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name='john'
    return render (request, 'index.html',{'name':name})

def counter(request):
    text=request.GET['text']
    amount=len(text.split())
    return render(request,'counter.html',{'amount':amount})   