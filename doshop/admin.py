from django.contrib import admin
from .models import Category, Product, Company

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','specialـprice','category','available') 
    list_filter  = ('available','created')
    list_editable = ('specialـprice',)
    raw_id_fields = ('category',)
    actions = ('make_avaliable',)

    def make_avaliable(self, request, queryset) :
        rows = queryset.update(available=True)
        self.messages_user(request, f'{rows} updated')
    
    make_avaliable.short_description = 'make all available'
    

