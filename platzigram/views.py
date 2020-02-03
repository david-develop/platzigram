"""Platzigram views."""

from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    """Return a message"""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hello, world current server time is {}'.format(now))

def int_sort(request):
    """Sort integers with a GET method"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_num = sorted(numbers)
    data = {
        'status': 'ok',
        'numbers': sorted_num,
        'message': 'Integers sorted successfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    """Return a greeting."""
    if age < 12:
        message = 'Sorry {}, you are under 12 years old'.format(name)
    else:
        message = 'Welcome to Platzigram {}'.format(name)
    return HttpResponse(message)