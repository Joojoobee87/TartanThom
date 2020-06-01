from django.test import TestCase

# Create your tests here.


class TestAboutViews(TestCase):

    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')

    def test_get_about_design_page(self):
        response = self.client.get('/about/design/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about_design.html')

    def test_get_about_philosphy_page(self):
        response = self.client.get('/about/philosophy/')
        self.assertEqual(response.status_code, 200)

