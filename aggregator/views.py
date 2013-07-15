from django.shortcuts import render

from aggregator import forms

def search(request):
    form = forms.PriceSearchForm()
    return render(request, 'aggregator/search.html', { 'form': form })
