from django import forms

from aggregator.engines.store_config import StoreConfig

class PriceSearchForm(forms.Form):
    q = forms.CharField(
        label='Search for',
        error_messages={'required': 'Please enter something to search for.'}
    )

    stores = StoreConfig.stores()
    store_choices = [ [store, store] for store in stores ]
    stores = forms.MultipleChoiceField(
        choices=store_choices,
        widget = forms.widgets.CheckboxSelectMultiple,
        initial = stores,
        label='In these stores'
    )
