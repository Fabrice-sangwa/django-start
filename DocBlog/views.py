from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def index(request):
    #return HttpResponse("<h1>Bienvenue sur mon site web</h1>")
    return render(request, "DocBlog/index.html", context={"name": "Fabrice", "date":datetime.today()})


