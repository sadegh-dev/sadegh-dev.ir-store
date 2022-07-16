from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline) :
    model = OrderItem
    raw_id_fields = ('product',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','total_price','created','paid')
    list_firlter = ('paid',)
    inlines = (OrderItemInline,)

