from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import requests

from .tasks import sendEmail

# Create your views here.

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1> Done Sending </h1>")


@cache_page(60)
def test(request):
    response = requests.get("https://bd21cd6d-7230-4eba-b356-fa27aecb7e7a.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())