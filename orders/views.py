from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.sessions import CartSessions
from django.contrib import messages


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if order.user.id == request.user.id or request.user.access_level == 'o':

        # session for order
        request.session['id_pay'] = order.id
        
        context = {
            'order' : order
        }
        return render(request,'orders/order_detail.html', context) 
    else :
        return redirect('doshop:home') 


 
@login_required
def order_create(request):
    cart = CartSessions(request)
    order = Order.objects.create(user=request.user, total_price=cart.get_total_price())
    for item in cart :
        OrderItem.objects.create(order=order, product=item['product'], price=item['price'], number=item['number'])
    cart.clear()
    return redirect('orders:order_detail', order.id)


@login_required
def order_list(request):
    orders = Order.objects.filter(user = request.user)
    context = {
        'orders' : orders
    }
    return render(request, 'orders/order_list.html' , context)



@login_required
def order_delete(request, order_id):
    the_order = get_object_or_404(Order, id = order_id)
    the_order.delete()
    messages.success(request, 'سفارش با موفقیت حذف شد','success')
    return redirect('orders:order_list')


