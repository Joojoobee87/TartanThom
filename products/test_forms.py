from django.test import TestCase
from products.forms import ReviewForm
from products.models import Products
from django.contrib.auth.models import User

# Create your tests here.

class TestReviewForm(TestCase):

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

    def test_review_text_is_required(self):
        form = ReviewForm({
            'review_text': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('review_text', form.errors.keys())
        self.assertEqual(form.errors['review_text'][0], "This field is required")

    def test_review_rating_is_required(self):
        form = ReviewForm({
            'review_rating': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], "This field is required")

    def test_min_value_of_review_rating(self):
        form = ReviewForm({
            'review_rating': 0
        })
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], "The minimum value is 1")

    def test_max_value_of_review_rating(self):
        form = ReviewForm({
            'review_rating': 10
        })
        self.assertFalse(form.is_valid())
        self.assertIn('review_rating', form.errors.keys())
        self.assertEqual(form.errors['review_rating'][0], "The maximum value is 5")

    def test_review_text_max_length(self):
        form = ReviewForm({
            'review_text': 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. At ducimus est eum odio consequatur in ipsa ipsam ullam accusantium dolorem? Mollitia facilis quisquam, voluptate iure facere numquam delectus nesciunt reiciendis. Lorem ipsum dolor sit amet consectetur, adipisicing elit. At ducimus est eum odio consequatur in ipsa ipsam ullam accusantium dolorem? Mollitia facilis quisquam, voluptate iure facere numquam delectus nesciunt reiciendis. Lorem ipsum dolor sit amet consectetur, adipisicing elit. At ducimus est eum odio consequatur in ipsa ipsam ullam accusantium dolorem? Mollitia facilis quisquam, voluptate iure facere numquam delectus nesciunt reiciendis.',
            'review_rating': 5,
        })
        self.assertFalse(form.is_valid())
        self.assertIn('review_text', form.errors.keys())
        self.assertEqual(form.errors['review_text'][0], "Try keep it short and sweet, maximum 500 characters")
