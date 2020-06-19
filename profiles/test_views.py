from django.test import TestCase

# Create your tests here.


class TestProfilesViews(TestCase):

    def test_view_profile_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_profile.html')

    def test_view_my_details_page(self):
        response = self.client.get('/my_details/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_details.html')

    def test_view_testimonials_page(self):
        response = self.client.get('/home/testimonial/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/testimonial.html')
