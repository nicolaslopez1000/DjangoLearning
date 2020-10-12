from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm


# Create your views here.


def home(request):
    orders_list = Order.objects.all()
    customers_list = Customer.objects.all()
    total_customers = customers_list.count()
    total_orders = orders_list.count()
    delivered = orders_list.filter(status='Delivered').count()
    pending = orders_list.filter(status='Pending').count()

    context = {'orders': orders_list, 'customers': customers_list,
               'total_customers': total_customers, 'delivered': delivered,
               'total_orders': total_orders, 'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    product_list = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': product_list})


def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}

    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        # print('Printing post: ', request.POST)
        form = OrderForm(request.POST,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)

    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html',context)