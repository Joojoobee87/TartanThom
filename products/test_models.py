from django.test import TestCase
from products.models import Products, ProductReviews
from django.contrib.auth.models import User
import datetime

# Create your tests here.

class TestProductsModels(TestCase):

    def setUp(self):

        self.user_1 = User.objects.create_user('test', 'test@test.com', 'test1234')

        self.product_1 = Products.objects.create(
            name='Test Card',
            image='media/img/NewHome.jpg',
            product_type='cards',
            category='Birthday',
            price=5.00,
            size='A5',
        )

        self.product_1_review = ProductReviews.objects.create(
            user=self.user_1,
            product=self.product_1,
            review_text="This is my review",
            review_rating=5,
        )

    def test_product_fields_with_default_false_attribute(self):
        self.assertFalse(self.product_1.is_active)
        self.assertFalse(self.product_1.is_bespoke)

    def test_product_fields_that_are_none(self):
        self.assertIsNone(self.product_1.sale_price)

    def test_product_fields_with_blank_string_value(self):
        self.assertEquals(self.product_1.description, '')
        self.assertEquals(self.product_1.tags, '')

    def test_products_string_method_returns_name(self):
        product = self.product_1.name
        self.assertEqual(str(product), 'Test Card')

    def test_product_review_active_on_create(self):
        self.assertTrue(self.product_1_review.review_active)

    def test_product_review_string_method_returns_user(self):
        user = self.product_1_review.user.username
        self.assertEqual(str(user), 'test')

    def test_get_review_percentage(self):
        self.product_1_review.review_rating = 4
        self.assertTrue(self.product_1_review.review_percentage, 80)

    def test_get_review_percentage_returns_int(self):
        percentage = self.product_1_review.review_percentage()
        self.assertIsInstance(percentage, int)

    def tearDown(self):
        self.product_1.delete()
        self.product_1_review.delete()
        self.user_1.delete()
