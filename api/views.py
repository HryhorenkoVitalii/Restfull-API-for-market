from django.utils.datastructures import MultiValueDictKeyError
from django.utils.datetime_safe import datetime
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .models import Products, Orders
from .serializers import ProductsSerializer, OrdersSerializer, BillsSerializer, StatisticSerializer
from .utils import amount_to_pay


class ApiProductViews(viewsets.ViewSet):

    def get_all_products(self, request):
        data = Products.objects.all()
        serializer = ProductsSerializer(data, many=True)
        return Response(serializer.data)

    def get_product(self, request, pk):
        product = get_object_or_404(Products.objects.all(), pk=pk)
        serializer = ProductsSerializer(product, many=False)
        return Response(serializer.data)

    def add_product(self, request):
        data = request.data
        serializer = ProductsSerializer(data=data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": "Product '{}' with id={} add successfully".format(data["name"],
                                                                             serializer.data["id"])
                }, status=201
            )
        else:
            return Response({
                "details": "invalid value"
                }, 400
            )

    def update_product(self, request, pk):
        product = get_object_or_404(Products.objects.all(), pk=pk)
        serializer = ProductsSerializer(instance=product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                    "success": "Product id = {} is update".format(serializer.data["id"])
                    }, 200)
        else:
            return Response({
                    "details": "invalid value"
                }, 400
            )

    def delete_product(self, request, pk):
        product = get_object_or_404(Products.objects.all(), pk=pk)
        product.delete()
        return Response({"detail": f"Products id={pk} is deleted"}, 200)


class ApiOrdersViews(viewsets.ViewSet):

    def get_all_orders(self, request):
        data = Orders.objects.all()
        serializer = OrdersSerializer(data, many=True)
        return Response(serializer.data)

    def get_order(self, request, pk):
        order = get_object_or_404(Orders.objects.all(), pk=pk)
        serializer = OrdersSerializer(order, many=False)
        return Response(serializer.data)

    def add_order(self, request):
        product = get_object_or_404(Products.objects.all(), pk=request.data["product_id"])
        order = Orders(product=product)
        order.save()
        return Response(request.data)

    def update_order(self, request, pk):
        order = get_object_or_404(Orders.objects.all(), pk=pk)
        serializer = OrdersSerializer(instance=order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                    "success": "Order id = {} is update".format(serializer.data["id"])
                    }, 200)
        else:
            return Response({
                    "details": "invalid value"
                }, 400
            )


    def delete_order(self, request, pk):
        order = get_object_or_404(Orders.objects.all(), pk=pk)
        order.delete()
        return Response({"detail": f"Order id={pk} is deleted"})


class ApiBillsViews(viewsets.ViewSet):

    def get_bill(self, request, pk):
        order = get_object_or_404(Orders.objects.all(), pk=pk)
        bill = {
            "title": order.product.name,
            "price": order.product.price,
            "discount": f"{order.product.discount} %",
            "amount_to_pay": amount_to_pay(order.product.discount,
                                           order.product.price),
            "date_order": order.date_created_order.strftime("%d-%m-%Y %H:%M:%S"),
            "date_bill": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }
        serializer = BillsSerializer(bill, many=False)
        return Response(serializer.data)


class ApiStatisticsViews(viewsets.ViewSet):

    parser_classes = (FormParser, MultiPartParser)

    def get_all_statistic(self, request):
        if request.method == "POST":
            data_from = datetime.strptime(request.data["from"], "%d-%m-%Y")
            orders = Orders.objects.filter(date_created_order__gte=data_from)
            # if user want use only data_from
            try:
                data_to = datetime.strptime(request.data["to"], "%d-%m-%Y")
                orders.filter(date_created_order__lte=data_to)
            except MultiValueDictKeyError:
                pass
        else:
            orders = Orders.objects.all()

        result = []

        for order in orders:
            statistic = {
                "order_id": order.id,
                "product": order.product,
                "date_order": order.date_created_order.strftime("%d-%m-%Y %H:%M:%S"),
                "status": order.status,
                "paid": order.paid,
                "amount_to_pay": amount_to_pay(float(order.product.discount),
                                               float(order.product.price))
            }
            result.append(statistic)
        serializer = StatisticSerializer(result, many=True)
        return Response(serializer.data)
