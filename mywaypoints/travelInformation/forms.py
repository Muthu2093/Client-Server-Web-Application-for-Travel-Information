from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class NameFormMain(forms.Form):
	from_location = forms.CharField(label='To', max_length=100)
	to_location = forms.CharField(label='From', max_length=100)