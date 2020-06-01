from django.test import TestCase, TransactionTestCase
from .forms import LoginForm, RegistrationForm

# Create your tests here.


class TestLoginForm(TestCase):

    def test_password_is_required(self):
        form = LoginForm({'username': 'test', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertIn(form.errors['password'][0], 'This field is required.')


class TestRegistrationForm(TestCase):

    def test_not_current_user(self):
        form = RegistrationForm({'email': 'test@test.com', 'username': 'test', 'password1': 'iamtesting', 'password2': 'iamtesting'})
        new_form = RegistrationForm({'email': 'test@test.com', 'username': 'test', 'password1': 'iamtesting', 'password2': 'iamtesting'})
        self.assertTrue(new_form.is_valid())

    def test_email_address_is_valid(self):
        form = RegistrationForm({'email': 'email.com', 'username': 'test', 'password1': 'iamtesting', 'password2': 'iamtesting'})
        self.assertFalse(form.is_valid())
        self.assertIn(form.errors['email'][0], 'Enter a valid email address.')

    def test_passwords_match(self):
        form = RegistrationForm({'email': 'test@test.com', 'username': 'test', 'password1': 'iamtesting', 'password2': 'iamtestin'})
        self.assertFalse(form.is_valid())
        self.assertIn(form.errors['password2'][0], "The two password fields didn’t match.")
