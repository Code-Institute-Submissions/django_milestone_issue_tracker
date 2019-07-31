from django.test import TestCase
from django.contrib.auth.models import User


class TestUserAuthViews(TestCase):

    # Set up test user account
    def authenticate(self):
        User.objects.create_user(username='testuser', password='password')
        return self.client.login(username='testuser', password='password')

    # Register user
    def test_registration_form(self):
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_user(self):
        data = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'password',
            'password2': 'password'
        }
        response = self.client.post('/accounts/register/',
                                    data, follow=True)
        self.assertContains(response, 'You have successfully registered', 1,
                            200)

    def test_user_exists(self):
        data = {
            'email': 'test@test.com',
            'username': 'test',
            'password1': 'password',
            'password2': 'password'
        }
        User.objects.create_user(username='test', email=data['email'],
                                 password='password')
        response = self.client.post('/accounts/register/', data, follow=True)
        self.assertContains(response, 'Email addresses is already registered.',
                            0, 200)

    # Login
    def test_can_login(self):
        auth_user = self.authenticate()
        self.assertTrue(auth_user)
        response = self.client.get('/', follow=True)
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_login_no_password(self):
        response = self.client.post('/accounts/login/', {'password': ''})
        self.assertContains(response, 'This field is required.', 2, 200)
        self.assertFormError(response, 'form', 'password',
                             u'This field is required.')

    def test_login_no_username(self):
        response = self.client.post('/accounts/login/',
                                    {'username_or_email': ''})
        self.assertContains(response, 'This field is required.', 2, 200)
        self.assertFormError(response, 'form', 'username_or_email',
                             u'This field is required.')

    def test_login_page(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_user_redirected_when_logged_in(self):
        self.authenticate()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Logout user
    def test_logout(self):
        self.authenticate()
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 302)

    def test_logout_message(self):
        self.authenticate()
        response = self.client.get('/accounts/logout/', follow=True)
        self.assertContains(response, 'You have successfully logged out', 1,
                            200)
