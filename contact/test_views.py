from django.test import TestCase

# Create your tests here.


class TestContactViews(TestCase):

    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_get_faq_page(self):
        response = self.client.get('/contact/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/faq.html')
