"""Platzigram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    """Return a greeting"""
    return HttpResponse(
        'Hello, the current time in the server is: {}'.format(
            str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))))

def sorted_json(request):
    """Return JSON response with sorted integers"""
    # Query - request

    # Correct but, the values are going to still in string
    request.GET['numbers'].split(',')
    # map to convert values in int's
    q = map(int, request.GET['numbers'].split(','))
    # Create a number list
    list_str = [number for number in q]
    list_str.sort()
    # 'Maybe' the easiest method
    list_str2 = [int(i) for i in request.GET['numbers'].split(',')]
    list_str2.sort()
    # Create a dictionarie
    numbers = dict(numbers = list_str2)
    #import pdb; pdb.set_trace() #Debugger
    data = {
        'status': 'ok',
        'numbers': list_str2,
        'message': 'Integers sorted succesfully'
    }
    #return HttpResponse(str(numbers), content_type='application/json')
    return JsonResponse(data, safe=False)

def say_hi(request, name, age):
    """Return a greeting"""
    if age < 12:
        message = 'Sorry {}, you are not allowed to enter here'.format(name)
    else:
        message = 'Hello {}, welcome to Platzigram'.format(name)
    return HttpResponse(message)