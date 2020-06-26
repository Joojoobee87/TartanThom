from django.test import TestCase
from .forms import OrderForm

# Create your tests here.


class TestCheckoutForms(TestCase):

    def test_fullname_required(self):
        form = OrderForm({'fullname': ''})
        self.assertFalse(form.is_valid())

    def test_fields_in_order_form_meta_class(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('fullname', 'phone_number', 'address_line1', 'address_line2', 'town_city', 'postcode', 'country'))

    def test_fields_in_bespoke_form_meta_class(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, ('person_name1', 'person_name2', 
        'date_of_birth', 'place_of_birth', 'birth_weight_lb', 'birth_weight_oz', 
        'address_line1'))
