from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.


class TestProfilesViews(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_view_profile_page(self):
        self.client.login(username='test', password='test1234')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_profile.html')

    def test_view_my_details_page(self):
        self.client.login(username='test', password='test1234')
        response = self.client.get('/profiles/my_details/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/my_details.html')

    def test_view_testimonials_page(self):
        self.client.login(username='test', password='test1234')
        response = self.client.get('/home/testimonial/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/testimonial.html')

    def tearDown(self):
        self.user_1.delete()
