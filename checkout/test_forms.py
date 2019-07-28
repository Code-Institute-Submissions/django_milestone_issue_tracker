from django.test import TestCase
from .forms import MakePaymentForm, OrderForm


class TestCheckoutForm(TestCase):

    def test_payment_form_valid(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': "123",
            'expiry_month': 3,
            'expiry_year': 2023,
            'stripe_id': 'a'
        })
        self.assertTrue(form.is_valid())

    def test_payment_form_invalid(self):
        form = MakePaymentForm({
            'credit_card_number': '4242424242424242',
            'cvv': "123",
            'expiry_month': 1,
            'expiry_year': 2008,
            'stripe_id': 'a'
        })
        self.assertFalse(form.is_valid())

    def test_details_form_valid(self):
        form = OrderForm({
            'full_name': 'Test User',
            'phone_number': '01234567890',
            'country': 'UK',
            'postcode': 'BN1 5PR',
            'town_or_city': 'Brighton',
            'street_address1': 'Example street',
            'street_address2': 'Test',
            'county': 'East Sussex'
        })
        self.assertTrue(form.is_valid())

    def test_details_form_invalid(self):
        form = OrderForm({
            'full_name': 'Test User',
            'phone_number': '01234567890',
            'country': 'UK',
            'postcode': 'BN1 5PR',
            'town_or_city': 'Brighton',
            'street_address1': 'Example street',
            'street_address2': '',
            'county': 'East Sussex'
        })
        self.assertFalse(form.is_valid())