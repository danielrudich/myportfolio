from django.shortcuts import render
from django.http import HttpResponse

from .models import Job


def index(request):
    jobs = Job.objects
    return render(request, 'jobs/index.html', {'jobs':jobs})
