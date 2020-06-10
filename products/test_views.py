from django.test import TestCase
from django.utils import timezone
from products.models import Products, ProductReviews
from django.contrib.auth.models import User

# Create your tests here.


class TestProductsViews(TestCase):

    def setUp(self):

        User.objects.create_user('test', 'test@test.com', 'test1234')
        user = User.objects.get(username='test')

        Products.objects.create(
            name='Test Card',
            image='media/img/NewHome.jpg',
            product_type='Cards',
            description='This is the description of the test card',
            category='Birthday',
            price=5.00,
            sale_price=0,
            size='A5',
            label='New',
            is_bespoke=False,
            is_active=True)
        product = Products.objects.get(name='Test Card')

        ProductReviews.objects.create(
            user=user.id,
            product=product.id,
            user_anonymous=False,
            review_text='This is the review text',
            review_rating=4,
            review_date=timezone.now(),
            review_active=True)

    def test_get_view_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_view_selected_product_page(self):
        response = self.client.get(f'/products/view-product/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')

