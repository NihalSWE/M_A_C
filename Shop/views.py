from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json


def base(request):
    return render(request, "shop/base.html")


def index(request):
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nslides), nslides])
    nihals = {'allprods': allprods}
    return render(request, "shop/index.html", nihals)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, description=desc)
        contact.save()
    return render(request, "shop/contact.html")


def tracker(request):
    if request.method == "POST":
        orderid = request.POST.get('orderid', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderid, email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=orderid)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates":updates, "itemsJson": order[0].items_json},
                                          default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"no item"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'shop/tracker.html')


def search(request):
    query = request.GET.get('search')
    allprods = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nslides), nslides])
    nihals = {'allprods': allprods, "msg": ""}
    if len(allprods) == 0 or len(query) < 4:
        nihals = {'msg': "Please make sure to enter relevant search query"}
    return render(request, "shop/search.html", nihals)


def searchMatch(query, item):
    if query in item.product_name or query in item.category:
        return True
    else:
        return False


def productview(request, myid):
    # Fetch product using the id
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productview.html", {'product': product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')
        order = Order(items_json=items_json, name=name, email=email, address=address, city=city, phone=phone)
        order.save()
        update = OrderUpdate(order_id=order, update_desc="The order has been placed")
        update.save()
        thank = True
        ord_id = order.order_id
        return render(request, "shop/checkout.html", {'thank': thank, 'ord_id': ord_id})
    return render(request, "shop/checkout.html")
