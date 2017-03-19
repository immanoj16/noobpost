from django.shortcuts import render, get_object_or_404
from .models import Tutorial


# Create your views here.
def tutorial(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, pk=tutorial_id)
    return render(request, 'tutorial/tutorial.html', {'tutorial': tutorial})