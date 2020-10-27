from django.shortcuts import render
from django.http import HttpResponse
import getpass

# Create your views here.
def index(request):
    return render (request, "Form/index.html")
