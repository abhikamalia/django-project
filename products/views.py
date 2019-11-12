from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	res = 'hello world....This is working fine...'
	return HttpResponse(res)

def new(request):
	res2 = 'this is a new page...'
	return HttpResponse(res2)