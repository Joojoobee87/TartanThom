from django import forms
from products.models import ProductReviews


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ProductReviews

        fields = ('review_rating', 'review_text', 'user_anonymous')

        widgets = {
            'review_rating': forms.NumberInput(attrs={'localize': False, 'min_value': 1, 'max_value': 5}),
            'review_text': forms.Textarea(attrs={'required': True, 'rows': 5, 'cols': 20, 'max_length': 500}),
            'user_anonymous': forms.CheckboxInput(attrs={'required': False, 'null': False}),
        }

        labels = {
            'review_rating': 'Rating',
            'review_text': 'Product Review',
            'user_anonymous': 'Prefer to remain anonymous?',
        }

        help_texts = {
            'review_rating': 'Enter a rating from 1-5 (1=Poor, 5=Excellent)',
            'review_text': 'Tell us a bit about why you love this product',
            'user_anonymous': 'Would you prefer your review to be anonymous to other customers?',
        }

        error_messages = {
            'review_text': {
                'max_length': "Try keep it short and sweet",
            },
        }
