from django.shortcuts import render


def welcome(request):
    return render(request, 'welcome/hello_app_engine.html')
