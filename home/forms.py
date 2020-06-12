from django import forms
from home.models import Testimonials


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials

        fields = ('testimonial', 'testimonial_allow_publish')

        widgets = {
            'testimonial': forms.Textarea(attrs={'required': True, 'rows': 5, 'cols': 20, 'max_length': 500}),
            'testimonial_allow_publish': forms.CheckboxInput(attrs={'required': False, 'null': False}),
        }

        labels = {
            'testimonial': 'Testimonial',
            'testimonial_allow_publish': 'Permission to publish',
        }

        help_texts = {
            'testimonial': 'Tell us a bit about why you love Tartan Thom',
            'testimonial_allow_publish': 'Do we have your permission to publish on our site?',
        }

        error_messages = {
            'testimonial': {
                'max_length': "Try keep it short and sweet",
            },
        }
