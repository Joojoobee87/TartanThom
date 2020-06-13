from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Testimonials(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'

    testimonial_date = models.DateField()
    testimonial_allow_publish = models.BooleanField(default=True)
    testimonial = models.TextField()
    testimonial_active = models.BooleanField(default=False)
    testimonial_user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
