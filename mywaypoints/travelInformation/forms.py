from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class NameFormMain(forms.Form):
	start = forms.CharField(label='To', max_length=100)
	end = forms.CharField(label='From', max_length=100)


class NameFormMain(forms.Form):
	start = forms.CharField(label='To', max_length=100)
	end = forms.CharField(label='From', max_length=100)

# class response_gmap(forms.Form):
	# geocoded_waypoints = forms.CharField(label='To', max_length=100)
	# routes = 
	# status = 