from django.http import HttpResponse

def start(request):
    return HttpResponse("Hello there")
