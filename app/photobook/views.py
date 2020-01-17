from django.shortcuts import render


def page(request):
    return render(request, 'page_1.html')


def index(request):
    return render(request, 'index.html')
