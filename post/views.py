from django.shortcuts import render
from tutorial.models import Tutorial


def index(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'index.html', {'tutorials': tutorials})


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def privacy(request):
    return render(request, 'privacy.html')


def terms(request):
    return render(request, 'terms.html')
