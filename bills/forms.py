from django import forms
from expenses.models import carat

carat_choices = (('23', '23'),
                 ('22', '22'), 
                 ('18', '18'),
                 ('14', '15'))
ornament_type_choices = (('gold', 'Gold'),
                         ('silver', 'Silver'))

item_choices = (('bracelet', 'Bracelet'),
                ('necklace', 'Necklace'),
                ('rings','Rings'),
                ('earpeice', 'EarPeice'))

class bill_form(forms.Form):
    item = forms.ChoiceField(choices=item_choices)
    weight = forms.FloatField(max_length = 2)
    carat = forms.ChoiceField(choices=carat_choices)
    cost = forms.FloatFielf(max_length=7) 
