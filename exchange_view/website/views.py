from django.http import HttpResponse


# noinspection PyUnusedLocal
def index(request):
    return HttpResponse('Hello, this is my first response')
