from dataclasses import asdict
import os
import logging

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
django.setup()

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic
from test_data_storage import *

logger = logging.getLogger('main')


def create_spend_data(spend_data: tuple):
    data = SpendItem(*spend_data)
    try:
        a = SpendStatistic.objects.create(**asdict(data))
    except Exception as e:
        logging.error(e)
        raise e
    return a


def create_revenue_data(revenue_data: tuple):
    data = RevenueItem(*revenue_data)
    try:
        a = RevenueStatistic.objects.create(**asdict(data))
    except Exception as e:
        logging.error(e)
        raise e
    return a


def main():
    spend1 = create_spend_data(("Product A", datetime.date(2023, 9, 1), 100.00, 5000, 200, 10))
    spend2 = create_spend_data(("Product A", datetime.date(2023, 9, 2), 120.00, 6000, 250, 12))
    create_revenue_data(("Product A", datetime.date(2023, 9, 1), 250.00, spend1))
    create_revenue_data(("Product A", datetime.date(2023, 9, 2), 280.00, spend2))


main()
