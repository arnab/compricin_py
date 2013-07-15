from django.shortcuts import render

def start(request):
    return render(request, 'aggregator/start.html')
