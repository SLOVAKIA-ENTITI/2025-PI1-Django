from django.shortcuts import render, HttpResponse
from.models import Student

def index(request):
    studenti = Student.objects.all()
    return render(request, 'skola/index.html', {"studenti":studenti})
    
















