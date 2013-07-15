from django import forms

STORES = [ 'flipkart', 'amazon.in', 'ebay.in', 'infibeam']

class PriceSearchForm(forms.Form):
    q = forms.CharField(label='Search for')
    store_choices = [ [store, store] for store in STORES ]
    stores = forms.MultipleChoiceField(
        choices=store_choices,
        widget = forms.widgets.CheckboxSelectMultiple,
        initial = STORES,
        label='In these stores'
    )
