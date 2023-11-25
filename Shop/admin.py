from django.contrib import admin
from .models import Product, Contact, Order, OrderUpdate


# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'category', 'price', 'publish_date']
    search_fields = ('product_name', 'category')


@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'description']
    search_fields = ('name', 'email')


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'items_json', 'name', 'address', 'phone']
    search_fields = ('order_id', 'name')


@admin.register(OrderUpdate)
class OrderUpdateModelAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'update_id', 'update_desc', 'timestamp']
    search_fields = ['order_id']
