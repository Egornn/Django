import datetime
import logging
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from internet_shop.forms import GoodsForm
from internet_shop.models import Client, Goods, Order

logger = logging.getLogger(__name__)


def get_clients(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'internet_shop/clients.html', context=context)


def get_goods(request):
    goods = Goods.objects.all()
    context = '\n'.join(str(g) for g in goods)
    return HttpResponse(context)


def get_orders(request):
    orders = Order.objects.all()
    context = '\n'.join(str(order) for order in orders)
    return HttpResponse(context)


def get_client_goods(request, client_id: int):
    COUNT_DAYS = 7
    start = datetime.date.today() - datetime.timedelta(days=COUNT_DAYS)
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client_id=client_id, create_at__gte=start)
    context = {
        'count_days': COUNT_DAYS,
        'client': client,
        'orders': orders
    }
    return render(request, 'internet_shop/client_goods.html', context=context)


def get_orders_by_client_id(request, client_id: int):
    orders = Order.objects.filter(client_id=client_id)
    if orders:
        context = '\n'.join(str(order) for order in orders)
    else:
        context = f'User with id: {client_id} has no orders'
    return HttpResponse(context)


def add_goods(request):
    message = ''
    if request.method == 'POST':
        form = GoodsForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            amount = form.cleaned_data['amount']
            image = form.cleaned_data['image']
            logger.info(f'Received {name=}, {description=}, {price=}, {amount=}, {image=}')
            goods = Goods(name=name, description=description, price=price, amount=amount, image=image)
            goods.save()
            message = 'Item was saved'
    else:
        form = GoodsForm()
    return render(request, 'internet_shop/goods_form.html',
                  {'form': form, 'message': message})


def delete_client(request, client_id: int):
    client = Client.objects.filter(pk=client_id)
    if client:
        client.delete()
        return HttpResponse('User removed')
    else:
        return HttpResponse('User not found')


def delete_goods(request, goods_id: int):
    goods = Goods.objects.filter(pk=goods_id)
    if goods:
        goods.delete()
        return HttpResponse('Item deleted')
    else:
        return HttpResponse('Item not found')


def delete_order(request, order_id: int):
    order = Order.objects.filter(pk=order_id)
    if order:
        order.delete()
        return HttpResponse('The order has been deleted')
    else:
        return HttpResponse('The order is not found')


def edit_client_name(request, client_id: int, name: str):
    client = Client.objects.filter(pk=client_id).first()
    if client:
        client.name = name
        client.save()
        return HttpResponse('User Name was changed')
    else:
        return HttpResponse('User not found')


def edit_goods_price(request, goods_id: int, price: int):
    goods = Goods.objects.filter(pk=goods_id).first()
    if goods:
        goods.price = price
        goods.save()
        return HttpResponse('Price updated')
    else:
        return HttpResponse('Price is not found')


def edit_order_goods_id(request, order_id: int, goods_id: int):
    order = Order.objects.filter(pk=order_id).first()
    goods = Goods.objects.filter(pk=goods_id).first()
    if order:
        order.goods_id = goods
        order.save()
        return HttpResponse('Item was changed')
    else:
        return HttpResponse('The order was not found')
