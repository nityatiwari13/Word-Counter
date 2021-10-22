from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def ans(request):
    txt = request.GET.get('text', 'default')
    for char in txt:
        amt = 1
        for char in txt:
            if(char == " "):
                amt = amt + 1
    param = {
        'ans' : amt
    }
    return render(request, 'answer.html', param)
