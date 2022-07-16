from django.core import paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Category, Product, Company
from orders.models import Order
from cart.forms import CartAddForm
from .forms import InsertProductForm, EditProductForm, EditPriceProductForm, EditAvailableProductForm

def home(request) :
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    companies = Company.objects.all()

    #pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products' : page_obj ,
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/home.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    categories = Category.objects.all()
    companies = Company.objects.all()
    form = CartAddForm()

    context = {
        'product' : product ,
        'categories' : categories ,
        'companies' : companies,
        'form' : form
    }
    return render(request,'doshop/product_detail.html',context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(available=True, category=category)
    categories = Category.objects.all()
    companies = Company.objects.all()

    #pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products':page_obj,
        'category' : category ,
        'categories' : categories ,
        'companies' : companies
    }
    return render(request,'doshop/category_detail.html',context)


def company_detail(request, slug):
    company = get_object_or_404(Company, slug=slug)
    products = Product.objects.filter(available=True, company=company)
    categories = Category.objects.all()
    companies = Company.objects.all()

    #pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products':page_obj,
        'company' : company ,
        'companies' : companies ,
        'categories' : categories
    }
    return render(request,'doshop/company_detail.html',context)


def all_specialـprice(request) :
    products = Product.objects.filter(available=True, specialـprice__isnull=False)
    categories = Category.objects.all()
    companies = Company.objects.all()

    #pagination
    paginator = Paginator(products, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products' : page_obj ,
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/specialـprice.html', context)


def page_not_found(request):
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'categories' : categories,
        'companies' : companies ,
    }
    return render(request,'doshop/404.html', context)



# ----------- Manager ------------------- # 
@login_required
def insert_product(request):
    if request.user.access_level == 'o' :
        if request.method=='POST':
            form = InsertProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request,'ثبت کالای جدید با موفقیت انجام شد','success')
                return redirect('doshop:home')
        else :
            form = InsertProductForm()
        context = {
            'form' : form
        }
        return render(request,'accounts/manager/insert_product.html',context)
    else :
        return redirect('doshop:home')



@login_required
def edit_product(request, slug):
    if request.user.access_level == 'o' :
        the_product = get_object_or_404(Product, slug=slug)
        if request.method=='POST':
            form = EditProductForm(request.POST, request.FILES, instance=the_product)
            if form.is_valid():
                slug = form.cleaned_data['slug']
                form.save()
                messages.success(request,'ویرایش مشخصات کالا با موفقیت انجام شد','success')
                return redirect('doshop:product-detail', slug )
        else :
            form = EditProductForm(instance=the_product)
        context = {
            'form' : form ,
        }
        return render(request,'accounts/manager/edit_product.html',context)
    else :
        return redirect('doshop:home')



@login_required
def edit_price_product(request, slug):
    if request.user.access_level == 'o' :
        the_product = get_object_or_404(Product, slug=slug)
        if request.method=='POST':
            form = EditPriceProductForm(request.POST, instance=the_product)
            if form.is_valid():
                form.save()
                messages.success(request,'تغییر قیمت کالا با موفقیت انجام شد','success')
                return redirect('doshop:product-detail', slug )
        else :
            form = EditPriceProductForm(instance=the_product)
        context = {
            'product': the_product,
            'form' : form ,
        }
        return render(request,'accounts/manager/edit_price_product.html',context)
    else :
        return redirect('doshop:home')



@login_required
def edit_available_product(request, slug):
    if request.user.access_level == 'o' :
        the_product = get_object_or_404(Product, slug=slug)
        if request.method=='POST':
            form = EditAvailableProductForm(request.POST, instance=the_product)
            if form.is_valid():
                form.save()
                available = form.cleaned_data['available']
                if available :  
                    messages.success(request,'وضعیت کالا فعال است','success')
                    return redirect('doshop:product-detail', slug )
                else :
                    messages.success(request,'وضعیت کالا به وضعیت غیرفعال تبدیل شد','success')
                    return redirect('doshop:home')
        else :
            form = EditAvailableProductForm(instance=the_product)
        context = {
            'product': the_product,
            'form' : form ,
        }
        return render(request,'accounts/manager/edit_available_product.html',context)
    else :
        return redirect('doshop:home')



def not_available_products(request):
    if request.user.access_level == 'o' :
        products = Product.objects.filter(available=False)
        context = {
            'products' : products ,
        }
        return render(request,'accounts/manager/not_available_products.html', context)
    else :
        return redirect('doshop:home')



def all_order_list(request):
    if request.user.access_level == 'o' :
        orders = Order.objects.all()

        #pagination
        paginator = Paginator(orders, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'orders' : page_obj,
        }
        return render(request, 'accounts/manager/all_order_list.html' , context)
    else :
        return redirect('doshop:home')

# ---------- EndManager --------------------- #