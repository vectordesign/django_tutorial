from django.shortcuts import render


def landing_view(request):
    return render(request, 'mysite/landing.html', {})
