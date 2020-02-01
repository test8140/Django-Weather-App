from django.shortcuts import render
import requests


def index(request):
    appid = 'a9d0ce4653a3d5bb5a14558470bb9082'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    return render(request, 'weather/index.html')