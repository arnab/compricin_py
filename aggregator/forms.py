from django import forms

class PriceSearchForm(forms.Form):
    STORES = [ 'flipkart', 'amazon.in', 'ebay.in', 'infibeam']

    q = forms.CharField(
        label='Search for',
        error_messages={'required': 'Please enter something to search for.'}
    )

    store_choices = [ [store, store] for store in STORES ]
    stores = forms.MultipleChoiceField(
        choices=store_choices,
        widget = forms.widgets.CheckboxSelectMultiple,
        initial = STORES,
        label='In these stores'
    )
