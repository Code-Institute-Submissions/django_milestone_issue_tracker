from django.test import TestCase
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Feature

class TestCheckoutViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    @staticmethod
    def create_test_feature(self):
        feature = Feature(name='Test', description='Test description', author=self.user)
        feature.save()
        return feature
    
    def create_test_checkout(self):
        feature = self.create_test_feature(self)
        data = {
            'quantity': 1
        }
        self.client.post('/cart/add/{}'.format(feature.id), data, follow=True)
    
    def test_checkout_page(self):
        self.create_test_checkout()
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')