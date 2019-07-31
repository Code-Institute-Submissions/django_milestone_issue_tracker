from django.test import TestCase
from .models import Order


class TestModels(TestCase):

    @staticmethod
    def create_test_order():
        return Order(
            full_name='Test User',
            phone_number='01234567890',
            country='UK',
            postcode='BN1 5PR',
            town_or_city='Brighton',
            street_address1='Example street',
            street_address2='Test',
            county='East Sussex',
            date='2-2019-07-27'
        )

    def test_order_model(self):
        order = self.create_test_order()
        self.assertEqual(Order.__str__(order), '{0}-{1}-Test User'.format(
            order.id, order.date
        ))
