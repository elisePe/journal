from django import forms

from entree.models import entrees,users


class writeForm(forms.ModelForm):
   class Meta:
     model = entrees
     fields = ['date', 'texte']


class signForm(forms.ModelForm):
   class Meta:
     model = users
     fields = ['name', 'passw']

class logForm(forms.ModelForm):
   class Meta:
     model = users
     fields = ['name', 'passw']