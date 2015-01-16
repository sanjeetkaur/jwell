from django import forms
from expenses.models import carat

class add_bills(forms.Form):
    ornament_type = forms.CharField(max_length=20)
    
