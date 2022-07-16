from django.shortcuts import render, get_object_or_404, redirect
from doshop.models import Product, Category, Company
from .sessions import CartSessions
from .forms import CartAddForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def cart_detail(request):
    cart = CartSessions(request)
    categories = Category.objects.all()
    companies = Company.objects.all()
    context = {
        'cart' : cart,
        'categories' : categories,
        'companies' : companies,
    }
    return render(request, 'cart/cart_detail.html', context)

 

@login_required
@require_POST
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = CartSessions(request)
    form = CartAddForm(request.POST)
    if form.is_valid():
        number = form.cleaned_data['number']
        cart.add(product=product, number = number)
        messages.success(request, 'با موفقیت به سبد خرید اضافه شد','success')
        return redirect('doshop:home')
    else :
        messages.error(request,'ثبت کالا به تعداد وارد شده امکان پذیر نیست','danger')



@login_required
def cart_remove(request, product_id):
    cart = CartSessions(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, 'کالا با موفقیت از سبد خرید حذف شد','warning')
    return redirect('cart:cart_detail')

