from django.contrib import admin
from .models import Testimonials

# Register your models here.


class TestimonialsAdmin(admin.ModelAdmin):
    model = Testimonials
    list_display = ('testimonial_user', 'testimonial_date',
                    'testimonial_active')


admin.site.register(Testimonials, TestimonialsAdmin)
