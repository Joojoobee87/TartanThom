from django import forms
from checkout.models import Order
from .models import Bespoke


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('fullname', 'phone_number', 'address_line1', 'address_line2', 'town_city', 'postcode', 'country')


class BespokeForm(forms.ModelForm):

    wedding_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2040)), required=False)
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2040)), required=False)

    class Meta:
        model = Bespoke

        fields = ('person_name1', 'person_name2', 'date_of_birth', 'place_of_birth', 'birth_weight_lb', 'birth_weight_oz', 'address_line1')

        labels = {
            'person_name1': 'Name',
            'person_name2': 'Name of Person 2',
            'date_of_birth': 'Date of Birth',
            'place_of_birth': 'Place of Birth',
            'birth_weight_lb': 'Birth Weight (lb)',
            'birth_weight_oz': 'Birth Weight (oz)',
            'wedding_date': 'Date of wedding',
            'address_line1': 'Address'
        }

        help_texts = {
            'birth_weight_lb': 'Enter birth weight pounds',
            'birth_weight_oz': 'Enter birth weight ounces',
            'address_line1': 'Enter house no and street name',
        }