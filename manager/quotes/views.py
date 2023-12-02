from django.shortcuts import render
from .models import info
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    data = info.objects.all()
    return render(request, 'quotes/index.html', {'info': data})

def add(request):
    person = request.POST.get('person')
    quote = request.POST.get('Quote')
    if person and quote:
        QUOTE = info(person=person, quote=quote)
        QUOTE.save()
        return HttpResponseRedirect('/quotes')
    return render(request, 'quotes/add.html')

def delete(request, id):
    info.objects.get(pk = id).delete()
    return HttpResponseRedirect('/quotes')