from django.test import TestCase
from django.utils import timezone
from products.models import Products, ProductReviews
from django.contrib.auth.models import User
from django.contrib import messages

# Create your tests here.


class TestProductsViews(TestCase):

    def setUp(self):

        self.user_1 = User.objects.create_user('test', 'test@test.com', 'test1234')
        self.product_1 = Products.objects.create(
            name='Test Card',
            image='media/img/NewHome.jpg',
            product_type='cards',
            description='This is the description of the test card',
            category='Birthday',
            price=5.00,
            sale_price=0,
            size='A5',
            label='New',
            is_bespoke=False,
            is_active=True
            )
        self.product_2 = Products.objects.create(
            name='Test Card2',
            image='media/img/NewHome.jpg',
            product_type='cake-toppers',
            description='This is the description of the test card2',
            category='Birthday',
            price=5.00,
            sale_price=0,
            size='A5',
            label='New',
            is_bespoke=False,
            is_active=True
            )

        self.product_3 = Products.objects.create(
            name='Test Card3',
            image='media/img/NewHome.jpg',
            product_type='gifts',
            description='This is the description of the test card3',
            category='Birthday',
            price=5.00,
            sale_price=0,
            size='A5',
            label='New',
            is_bespoke=False,
            is_active=True
            )

    def test_get_view_products_page(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_view_selected_product_page(self):
        response = self.client.get(f'/products/view-product/{self.product_1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product.html')

    def test_get_view_products_by_type_cards(self):
        response = self.client.get(f'/products/products_by_type/{self.product_1.product_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_view_products_by_type_cake_toppers(self):
        response = self.client.get(f'/products/products_by_type/{self.product_2.product_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_view_products_by_type_gifts(self):
        response = self.client.get(f'/products/products_by_type/{self.product_3.product_type}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_count_total_no_of_products(self):
        results_count = Products.objects.all().count()
        self.assertEqual(results_count, 3)

    def test_count_total_no_of_cards_products(self):
        results_count = Products.objects.filter(product_type=self.product_1.product_type).count()
        self.assertEqual(results_count, 1)

    def test_count_total_no_of_cake_toppers_products(self):
        results_count = Products.objects.filter(product_type=self.product_2.product_type).count()
        self.assertEqual(results_count, 1)

    def test_count_total_no_of_gifts_products(self):
        results_count = Products.objects.filter(product_type=self.product_3.product_type).count()
        self.assertEqual(results_count, 1)

    def test_get_review_product_page(self):
        response = self.client.get(f'/products/review-product/{self.product_1.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/review_product.html')

    def tearDown(self):
        self.product_1.delete()
        self.product_2.delete()
        self.product_3.delete()
