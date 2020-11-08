from django import forms
from django.http import HttpResponse


class NameForm(forms.Form):

        comm = forms.CharField(label="Тема:", max_length=100)
	#message = forms.CharField(widget=forms.Textarea)
	#sender = forms.EmailField()
	#cc_myself = forms.BooleanField(required=False)
        response = HttpResponse()
        response.write("<p> HACK </p>")

