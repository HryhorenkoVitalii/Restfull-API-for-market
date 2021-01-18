from django.urls import path
from api.views import ApiProductViews, ApiOrdersViews, ApiBillsViews, ApiStatisticsViews


urlpatterns = [
    path("product/", ApiProductViews.as_view({"get": "get_all_products",
                                              "post": "add_product"})),
    path("product/<int:pk>", ApiProductViews.as_view({"get": "get_product",
                                                      "put": "update_product",
                                                      "delete": "delete_product"})),
    path("order/", ApiOrdersViews.as_view({"get": "get_all_orders",
                                           "post": "add_order"})),
    path("order/<int:pk>", ApiOrdersViews.as_view({"get": "get_order",
                                                   "put": "update_order",
                                                   "delete": "delete_order"})),
    path("bill/<int:pk>", ApiBillsViews.as_view({"get": "get_bill"})),
    path("statistic/", ApiStatisticsViews.as_view({"get": "get_all_statistic",
                                                   "post": "get_all_statistic"})),
]