from django.shortcuts import render


def interface(request):
    return render(request, 'meow/meow.html', {})


def profile(request):
    return render(request, 'meow/profile.html', {})
