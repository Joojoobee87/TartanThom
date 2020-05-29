from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('fullname', 'phone_number', 'address_line1', 'address_line2', 'town_city', 'postcode', 'country')
