from django.shortcuts import render

from aggregator import forms

def start(request):
    form = forms.PriceSearchForm()
    return render(request, 'aggregator/start.html', { 'form': form })
