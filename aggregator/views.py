from django.views.decorators.http import require_safe
from django.shortcuts import render

from aggregator import forms
from aggregator.engines.price_aggregator import PriceAggregator

@require_safe
def search(request):
    if len(request.GET) > 0:
        form = forms.PriceSearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            stores = form.cleaned_data['stores']
            PriceAggregator(q, stores).aggregated_prices()
    else:
        form = forms.PriceSearchForm()
    return render(request, 'aggregator/search.html', { 'form': form })
