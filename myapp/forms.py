from django import forms    

class SubscribeForm(forms.Form):
    mail = forms.CharField(label="Your Email", max_length=100, widget=forms.TextInput(attrs={'class':'form-control mb-3', 'id':'form-mail'}))
    message = forms.CharField(label="Your Message", widget=forms.Textarea(attrs={'class':'form-control','rows':'7'}))
