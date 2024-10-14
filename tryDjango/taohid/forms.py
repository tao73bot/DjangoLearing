from django import forms
from .models import TaoihdDetails

class TaohidForm(forms.Form):
    taohid_details = forms.ModelChoiceField(queryset=TaoihdDetails.objects.all(),label='Select Taohid')
    
