import os, csv
from pagination.settings import BUS_STATION_CSV
from django.shortcuts import render, redirect
from django.urls import reverse

BUSSTATIONS_LIST = []

def index(request):
    if len(BUSSTATIONS_LIST) == 0:
        load_stations(BUS_STATION_CSV)
    return redirect(reverse('bus_stations'))

# функция загрузки списка остановок
def load_stations(fname: str):
    if os.path.isfile(fname):
        with open(fname, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for raw in reader:
                BUSSTATIONS_LIST.append(raw)
# end load_stations()


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
    #     'bus_stations': ...,
    #     'page': ...,
    }
    return render(request, 'stations/index.html', context)
 