from django.db import models
from django.urls import reverse


class Category(models.Model):
    name =      models.CharField(max_length=400)
    slug =      models.SlugField(max_length=500, unique=True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'category' #name class for one
        verbose_name_plural = 'categories' #name class for all

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('doshop:category-detail', args=[self.slug,])



class Company(models.Model):
    name =      models.CharField(max_length=400)
    slug =      models.SlugField(max_length=500, unique=True)

    class Meta :
        ordering = ('name',)
        verbose_name = 'company' #name class for one
        verbose_name_plural = 'companies' #name class for all

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('doshop:company-detail', args=[self.slug,])



class Product(models.Model):
    category =      models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    company =       models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products', null=True)
    name =          models.CharField(max_length=400)
    slug =          models.SlugField(max_length=500, unique=True)
    image =         models.ImageField(upload_to='products/%Y/%m/%d/')
    description =   models.TextField()
    price =         models.IntegerField()
    number =        models.IntegerField(default=1)
    specialـprice = models.IntegerField(null=True, blank=True)
    available =     models.BooleanField(default=True)
    created =       models.DateTimeField(auto_now_add=True)
    updated =       models.DateTimeField(auto_now=True)

    class Meta :
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('doshop:product-detail', args=[self.slug,])



