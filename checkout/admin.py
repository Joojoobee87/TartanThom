from django.contrib import admin
from .models import Order, OrderItem, Bespoke

# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItem

    readonly_fields = ('item_total',)


class BespokeAdminInline(admin.TabularInline):
    model = Bespoke

    readonly_fields = ('product_name', )

    fields = ('bespoke_order', 'product_name', 'person_name1', 'person_name2', 'date_of_birth', 'place_of_birth', 'birth_weight_lb', 'birth_weight_oz', 'wedding_date', 'address_line1', 'is_complete')

    def product_name(self, instance):
        return instance.bespoke_product.name


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline, BespokeAdminInline)

    list_display = ('order_number', 'fullname', 'date', 'is_complete')

    readonly_fields = ('order_number', 'date')

    fields = ('order_user', 'order_number', 'date', 'fullname', 'phone_number', 
              'address_line1', 'address_line2', 'town_city', 'postcode', 'country', 'is_complete')





admin.site.register(Order, OrderAdmin,)
