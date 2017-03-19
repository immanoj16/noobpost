from django.shortcuts import render
from tutorial.models import Tutorial


def index(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'index.html', {'tutorials': tutorials})
