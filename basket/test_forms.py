from django.test import TestCase
from basket.forms import QuantityForm

# Create your tests here.


class TestBasketForms(TestCase):

    def test_quantity_form(self):
        form_data = {'quantity': '5'}
        form = QuantityForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_quantity_form_error_where_value_zero(self):
        form_data = {'quantity': '0'}
        form = QuantityForm(data=form_data)
        self.assertFalse(form.is_valid())
