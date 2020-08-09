from django.shortcuts import render
from app.models import Car

from django.views.generic import ListView, CreateView, View, FormView

from django.http import HttpResponse
from app.filters import CarFilter
import logging

logger = logging.getLogger(__name__)


def car_list(request):
    filtered = CarFilter(request.GET, queryset=Car.objects.all())
    logger.info(f'app - views - car_list filtered {filtered.__dict__}')
    return render(request, 'base.html', {'filter': filtered})
