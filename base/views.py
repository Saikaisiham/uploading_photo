from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index_page(request):
    return render(request, 'base/index.html')