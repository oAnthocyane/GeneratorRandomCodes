from django.http import HttpResponse
import random


def generate_code(request):
    code = random.randint(1000, 10000)
    return HttpResponse(code)
