from django.shortcuts import render
from courses.models import Courses, Tags
def home(request):
    courses = Courses.objects.all()
    return render(request, 'home.html', {'courses': courses})

def about(request):
    return render(request, 'about.html', {})
