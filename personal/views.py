from django.shortcuts import render

def index(request):
    return render(request, 'personal/new.html')


def contact(request):
    return render(request,'presonal/basic.html', {'content':['hi']})
