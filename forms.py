from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your first name', max_length=100)