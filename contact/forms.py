from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=80)
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        label='Your Message', widget=forms.Textarea(attrs={'rows': 5}))
