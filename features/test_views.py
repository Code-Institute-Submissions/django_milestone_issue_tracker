from django.test import TestCase
from django.contrib.auth.models import User
from .models import Feature


class TestFeatureViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username',
                                             password='password')
        self.client.login(username='username', password='password')

    @staticmethod
    def create_test_feature(self):
        feature = Feature(name='Test', description='Test description',
                          author=self.user)
        feature.save()
        return feature

    def test_feature_page(self):
        response = self.client.get('/features/all/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'features.html')

    def test_feature_detail_page(self):
        feature = self.create_test_feature(self)
        response = self.client.get('/features/{}/'.format(feature.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feature_detail.html')

    def test_feature_request_page(self):
        response = self.client.get('/features/feature-request/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'feature_request_form.html')

    def test_comment_feature(self):
        feature = self.create_test_feature(self)
        data = {
            'content': 'test comment'
        }
        response = self.client.post('/features/{}/'.format(feature.id), data,
                                    follow=True)
        self.assertContains(response, 'You have successfully posted a comment',
                            1, 200)
