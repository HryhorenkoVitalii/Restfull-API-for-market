from celery import shared_task
from django.utils.datetime_safe import datetime
from dateutil.relativedelta import relativedelta
from api.models import Products


@shared_task
def discount():
    products = Products.objects.all()
    now = datetime.now()
    for product in products:
        mounth = now + relativedelta(months=1)
        if product.date_added >= mounth:
            product.discount = 20
            product.save()
