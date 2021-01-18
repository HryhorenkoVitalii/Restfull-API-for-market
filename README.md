<h1 align="center">
   <br>
  <a><img src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/135056738/original/f4a1f882db100ea22db39e053f0f3a942654378e/create-you-a-rest-api.png" alt="logo" width="250"></a>
  <br>
  <br>
  Restfull API for internet market
  <br>
</h1>

### Description
To implement the system of monthly discounts I used "Celery" with every day check up data of add product and if it added last month add 20% discounts. So that the accountant can make a selection by dates to endpoint ```/api/atatistic/``` it is possible to make a post request with ```date_from``` and ```date_to``` in day-mounth-year format (exemple: ```date_from=10-11-2020``` ). Tests were implemented to check performance during development. The database already contains 1 product and 1 order

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/17c5428b5a421fe73ff3#?env%5BLight_IT_test_task%5D=W3sia2V5IjoibG9jYWwiLCJ2YWx1ZSI6Imh0dHA6Ly8xMjcuMC4wLjE6ODAwMCIsImVuYWJsZWQiOnRydWV9XQ==)

### Endpoints
```bash
# GET to view all products, POST to creae new.
/api/product/

# GET to view product id=pk, PUT to update product, DELETE to delete product.
api/product//<int:pk>

# GET to view all order, POST with id product to creae new order.Example json request {"product_id": 1}
api/order/

# GET to view order id=pk, PUT to update order, DELETE to delete order.
api/order/<int:pk>

# GET to bill based on order.Example endpoint "api/bill/1" for make bill based on order_id = 1 
api/bill/<int:pk>

# GET to view all statistic, POST with application/x-www-form-urlencoded date_from,date_to.Example POST application/x-www-form-urlencoded request: date_from=10-11-2020&date_to=15-11-2020
api/statistic/
```

## Credits

This software uses the following open source packages:

- [Django](https://www.djangoproject.com/)
- [djangorestframework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/en/stable/)
