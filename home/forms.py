from django import forms
from home.models import Testimonials


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonials

        fields = ('testimonial_date', 'testimonial_allow_publish', 'testimonial')

        widgets = {
            'testimonial': forms.Textarea(attrs={'rows': 5}),
            'testimonial_allow_publish': forms.CheckboxInput(default=False),
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
            'name': {
                'max_length': "This writer's name is too long.",
            },
        }
