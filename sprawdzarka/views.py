# Create your views here.
from django.shortcuts import render_to_response

def index(request):
	lista = [1,2,3,4]
	return render_to_response('index.html',{'lista': lista})
