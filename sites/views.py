from django.shortcuts import render
from .models import Site


def index(request):
    sites = Site.objects.all()
    context = {'sites': sites}
    return render(request, 'sites/index.html', context)
