from django import forms
from django.db import models
from .models import Search

from functools import partial
from django.utils.translation import ugettext_lazy as _
#Define a search class It will generate the search form automatically

#Dfine a new widget to enableing DatePicker css
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class SearchForm(forms.ModelForm):

    class Meta:
        model = Search
        fields = ('dep_date', 'ret_date','org_1','org_2')
        widgets = {
            'dep_date': DateInput(),
            'ret_date': DateInput(),
        }
        
        labels = {
            'dep_date':_('Departure:'),
            'ret_date':_('Return:'),
            'org_1':_('Place A'),
            'org_2':_('Place B'),
            
        }
        
        
