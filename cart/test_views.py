from django.test import TestCase
from django.contrib.auth.models import User
from features.models import Feature

class TestCartViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username', password='password')
        self.client.login(username='username', password='password')

    @staticmethod
    def create_test_feature(self):
        feature = Feature(name='Test', description='Test description', author=self.user)
        feature.save()
        return feature

    # Test pages
    def test_cart_page_status(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')

    # Add to cart
    def test_add_cart_status(self):
        feature = self.create_test_feature(self)
        data = {
            'quantity': 1
        }
        response = self.client.post('/cart/add/{}/'.format(feature.id), data, follow=True)
        self.assertEqual(response.status_code, 200)

    # Adjust quantity in cart
    def test_adjust_cart_quantity(self):
        feature = self.create_test_feature(self)
        initial_data = {
            'quantity': 1
        }
        self.client.post('/cart/add/{}/'.format(feature.id), initial_data, follow=True)
        data = {
            'quantity': 3
        }
        response = self.client.post('/cart/adjust/{}/'.format(feature.id), data, follow=True)
        self.assertEqual(response.status_code, 200)
