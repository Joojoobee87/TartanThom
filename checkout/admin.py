from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemsInline(admin.TabularInline):
    model = OrderItem

    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemsInline, )

    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_user', 'order_number', 'date', 'fullname', 'phone_number', 
              'address_line1', 'address_line2', 'town_city', 'postcode', 'country', 'order_total')


admin.site.register(Order, OrderAdmin)
