from django import forms
from .models import Product

class InsertProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =( 'category', 'company', 'name', 'slug', 'image', 'description', 'price', 'specialـprice')
        widgets = {
            'category':forms.Select(attrs={
                'class' :'form-control' ,
            }),
            'company':forms.Select(attrs={
                'class' :'form-control' ,
            }),
            'name':forms.TextInput(attrs={
                'class' :'form-control bg-light' ,
            }),
            'slug':forms.TextInput(attrs={
                'class' :'form-control bg-light text-start' ,
            }),
            'image':forms.FileInput(attrs={
                'class' :'form-control' ,
            }),
            'description':forms.Textarea(attrs={
                'class' :'form-control' ,
            }),
            'price':forms.TextInput(attrs={
                'class' :'form-control bg-light text-start' ,
            }),
            'specialـprice':forms.TextInput(attrs={
                'class' :'form-control bg-light text-start' ,
            }),
        }
        labels = {
            'category' : 'نوع',
            'company' : 'شرکت سازنده',
            'name' : 'نام محصول',
            'slug' : 'آدرس url',
            'image' : 'عکس',
            'description' : 'توضیحات',
            'price' : 'قیمت',
            'specialـprice' : 'قیمت فروش ویژه',
        }
        error_messages = {
            'slug':{
                'unique':'قبلا محصولی با این آدرس ثبت شده است',
                'invalid' : 'این فیلد شامل حروف انگلیسی و عدد و _ می تواند باشد.' ,
            },
            'price':{
                'invalid' : 'لطفا قیمت صحیح وارد نمایید' ,
            },
            'specialـprice':{
                'invalid' : 'لطفا قیمت صحیح وارد نمایید' ,
            },
        }



class EditProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =( 'category', 'company', 'name', 'slug', 'image', 'description')
        widgets = {
            'category':forms.Select(attrs={
                'class' :'form-control' ,
            }),
            'company':forms.Select(attrs={
                'class' :'form-control' ,
            }),
            'name':forms.TextInput(attrs={
                'class' :'form-control bg-light' ,
            }),
            'slug':forms.TextInput(attrs={
                'class' :'form-control bg-light text-start' ,
            }),
            'image':forms.FileInput(attrs={
                'class' :'form-control' ,
            }),
            'description':forms.Textarea(attrs={
                'class' :'form-control' ,
            }),
        }
        labels = {
            'category' : 'نوع',
            'company' : 'شرکت سازنده',
            'name' : 'نام محصول',
            'slug' : 'آدرس url',
            'image' : 'عکس',
            'description' : 'توضیحات',
        }
        error_messages = {
            'slug':{
                'unique':'قبلا محصولی با این آدرس ثبت شده است',
                'invalid' : 'این فیلد شامل حروف انگلیسی و عدد و _ می تواند باشد.' ,
            },
        }



class EditPriceProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('price', 'specialـprice')
        widgets = {
            'price':forms.TextInput(attrs={
                'class' :'form-control bg-light text-center w-25 ' ,
            }),
            'specialـprice':forms.TextInput(attrs={
                'class' :'form-control bg-light text-center w-25 ' ,
            }),
        }
        labels = {
            'price' : 'قیمت',
            'specialـprice' : 'قیمت فروش ویژه',
        }
        error_messages = {
            'price':{
                'invalid' : 'لطفا قیمت صحیح وارد نمایید' ,
            },
            'specialـprice':{
                'invalid' : 'لطفا قیمت صحیح وارد نمایید' ,
            },
        }

class EditAvailableProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields =('available',)
        labels = {
            'price' : 'وضعیت',
        }



