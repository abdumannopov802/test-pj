from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    
admin.site.register(Product, ProductAdmin)