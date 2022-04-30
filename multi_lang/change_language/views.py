from django.shortcuts import render
from .models import Example


def index(request):
    objects = Example.objects.all()
    return render(request, 'change_language/index.html', {'objects': objects})
