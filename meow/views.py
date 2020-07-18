from django.shortcuts import render


def interface(request):
    return render(request, 'meow/meow.html', {})


def login(request):
    return render(request, 'registration/login.html', {})
