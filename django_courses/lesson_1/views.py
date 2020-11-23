from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!!! Страница номер 1.")