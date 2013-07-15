from django.shortcuts import render

from aggregator import forms

def search(request):
    if len(request.GET) > 0:
        form = forms.PriceSearchForm(request.GET)
    else:
        form = forms.PriceSearchForm()
    return render(request, 'aggregator/search.html', { 'form': form })
