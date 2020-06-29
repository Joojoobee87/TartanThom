from django.test import TestCase
from products.models import Products

# Create your tests here.


class TestBasketViews(TestCase):

    def setUp(self):
        self.item = Products.objects.create(
            name='Happy Birthday',
            product_type='cards',
            image='img/CardHappyBirthday.jpg',
            description='Some description',
            category='Birthday',
            price=1.99,
            sale_price=0.99,
            size='A4',
            label='some label',
            tags='some tags',
            is_bespoke=False,
            is_active=True,
            )
        self.quantity = 1
        self.basket = {
            'item': self.item,
            'quantity': self.quantity,
        }
        print(self.basket)

    def test_view_basket(self):
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_amend_basket(self):
        response = self.client.get(f'/basket/amend/{self.item.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
