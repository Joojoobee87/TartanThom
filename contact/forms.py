from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=80)
    email = forms.EmailField(label='Email')
    message = forms.TextField(label='Your Message')
