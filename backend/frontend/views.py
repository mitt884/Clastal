from django.shortcuts import render
from courses.models import Courses
def home(request):
    course = Courses.objects.all()
    return render(request, 'home.html', {'courses': course})

def about(request):
    return render(request, 'about.html', {})