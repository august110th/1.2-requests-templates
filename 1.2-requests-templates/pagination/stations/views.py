import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):

    with open(settings.BUS_STATION_CSV, encoding='Utf-8', newline='') as f:
        file_reader = csv.DictReader(f)
        content = list(file_reader)
        current_page = int(request.GET.get('page', 1))
        paginator = Paginator(content, 10)
        page = paginator.get_page(current_page)
        page_content = page.object_list

        context = {
            'bus_stations': page_content,
            'page': page
        }
        return render(request, 'stations/index.html', context)
