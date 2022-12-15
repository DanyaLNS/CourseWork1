from django.http import HttpResponse
# Create your views here.
from app.read_csv.func import read


def index(request, s):
    return HttpResponse(f'{read(s)}')

