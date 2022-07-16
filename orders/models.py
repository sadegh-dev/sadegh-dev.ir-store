from django.db import models
from django.conf import settings
from doshop.models import Product


class Order(models.Model):
    user =      models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)
    total_price = models.IntegerField(null=True, default=True)
    paid =      models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.user}- {self.total_price} - {self.created}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())
    


class OrderItem(models.Model):
    order =     models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product =   models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    price =     models.IntegerField()
    number =    models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.product} - {self.number} - {self.price}'
    
    def get_cost(self):
        return self.price * self.number





