import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


def index(request):
    return redirect(reverse('bus_stations'))


# def bus_stations(request):
#     # получите текущую страницу и передайте ее в контекст
#     # также передайте в контекст список станций на странице
#
#     context = {
#     #     'bus_stations': ...,
#     #     'page': ...,
#     }
#     return render(request, 'stations/index.html', context)

def bus_stations(request):
    # Чтение CSV-файла
    with open(settings.BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Преобразование данных из CSV в список словарей
        stations_list = list(reader)

    # Получение номера текущей страницы из запроса
    current_page_number = request.GET.get('page', 1)

    # Создание объекта Paginator
    paginator = Paginator(stations_list, 10)  #  10 станций на страницу
    current_page = paginator.get_page(current_page_number)

    # Формирование контекста для шаблона
    context = {
        'bus_stations': current_page.object_list,  # Список станций на текущей странице
        'page': current_page,  # Текущая страница и её свойства
    }

    return render(request, 'stations/index.html', context)