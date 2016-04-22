from django import forms

class DecimalForm(forms.Form):
    dec = forms.FloatField(label='Decimal Odd', initial=1)
    frac = forms.CharField(label='Fractional Odd', initial=1)