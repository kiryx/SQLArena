# Create your views here.
from django.shortcuts import render_to_response
from django.template import loader, Context
from django.http import HttpResponse
from SQLArena.sprawdzarka.models import Baza

def index(request):
	lista = [1,2,3,4]
	return render_to_response('index.html',{'lista': lista})

def news(request):
	baza = Baza.objects.all()
	t = loader.get_template("news.html")
	c = Context({ 'baza': baza })
	return HttpResponse(t.render(c))