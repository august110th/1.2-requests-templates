import csv

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    f = open('C:\data-398-2018-08-30.csv', encoding='Utf-8', newline='')
    file_reader = csv.DictReader(f)
    content = list(file_reader)
    current_page = request.GET.get('page', 1)
    paginator = Paginator(content, 10)
    page = paginator.get_page(current_page)

    context = {
        'bus_stations': content,
        'page': page
    }
    return render(request, 'stations/index.html', context)
