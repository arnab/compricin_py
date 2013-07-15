from django.views.decorators.http import require_safe
from django.shortcuts import render

from aggregator import forms

@require_safe
def search(request):
    if len(request.GET) > 0:
        form = forms.PriceSearchForm(request.GET)
    else:
        form = forms.PriceSearchForm()
    return render(request, 'aggregator/search.html', { 'form': form })
