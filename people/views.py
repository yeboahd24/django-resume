from django.shortcuts import render
from django.shortcuts import get_object_or_404
from people.models import Person

def resume(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'resume.html', {'person': person})


