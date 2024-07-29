from django.shortcuts import render
from django.http import HttpResponse
from .tasks import sendEmail

# Create your views here.

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1> Done Sending </h1>")