from rest_framework.test import APITestCase
from rest_framework import status

from api.models import Products, Orders


class  ProductTestCase(APITestCase):

    def test_add_new_product(self):
        data = {"name": "New_product", "price": 20.01}
        response = self.client.post("/api/product/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_new_product_incorrect_price(self):
        data = {"name": "New_product", "price": 20.44401}
        response = self.client.post("/api/product/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_new_product_incorrect_discount(self):
        data = {"name": "New_product", "price": 20.44401, "discount": 200}
        response = self.client.post("/api/product/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_all_products(self):
        response = self.client.get("/api/product/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_product(self):
        data = {"name": "New_product", "price": 20.01}
        self.client.post("/api/product/", data)
        response = self.client.get("/api/product/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_product(self):
        data = {"name": "New_product", "price": 20.01}
        update_data = {"discount": 20}
        response_data = {'success': 'Product id = 1 is update'}
        self.client.post("/api/product/", data)
        response = self.client.put("/api/product/1", update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, response_data)

    def test_delete_product(self):
        data = {"name": "New_product", "price": 20.01}
        self.client.post("/api/product/", data)
        response = self.client.delete("/api/product/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class OrderTestCase(APITestCase):

    def setUp(self):
        Products.objects.create(name="New_product", price=20.01)

    def test_add_order(self):
        data_order = {"product_id": 1}
        response = self.client.post("/api/order/", data_order)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_orders(self):
        response = self.client.get("/api/product/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_order(self):
        data_order = {"product_id": 1}
        self.client.post("/api/order/", data_order)

        response = self.client.get("/api/order/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_order(self):
        data_order = {"product_id": 1}
        self.client.post("/api/order/", data_order)

        update_date = {"status": "done"}

        response = self.client.put("/api/order/1", update_date)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = {"success": "Order id = 1 is update"}
        self.assertEqual(response.data, response_data)

    def test_delete_order(self):
        data_order = {"product_id": 1}
        self.client.post("/api/order/", data_order)

        response = self.client.delete("/api/order/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BillsTestCase(APITestCase):

    def setUp(self):
        p = Products.objects.create(name="New_product", price=20.01)
        Orders.objects.create(product=p)


    def test_get_bill(self):
        response = self.client.get("/api/bill/1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_false_bill(self):
        response = self.client.get("/api/bill/35")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class StatisticTestCase(APITestCase):

    def setUp(self):
        p = Products.objects.create(name="New_product", price=20.01)
        Orders.objects.create(product=p)

    def test_statistic(self):
        response = self.client.get("/api/statistic/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
