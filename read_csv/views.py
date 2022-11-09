from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from read_csv.func import read


def index(request, s):
    return HttpResponse(f'{read(s)}')

