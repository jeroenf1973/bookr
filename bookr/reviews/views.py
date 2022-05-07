from urllib import request
from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse 
# Geen eigen http resonse opbject meer, deze gaan we maken via de render functie
from django.shortcuts import render

def index(request):
    #name = request.GET.get("name") or "world"
    #return HttpResponse(f"Hello {name}!")
    name = "Jeroen"
    #return render(request, "base.html", {"name": name})
    return render(request, "base.html")

def book_search(request):
    search_text = request.GET.get("search")
    return render(request, "book-search.html", {"search_text": search_text})


