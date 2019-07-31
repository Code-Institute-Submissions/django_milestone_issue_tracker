from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestUserAuthForms(TestCase):

    def test_login_with_correct_values(self):
        form = UserLoginForm({'username_or_email': 'test@test.com',
                              'password': 'test_password'})
        self.assertTrue(form.is_valid())

    def test_valid_login_form(self):
        form = UserLoginForm({
            'username_or_email': 'test@test.com',
            'password': 'password'

        })
        self.assertTrue(form.is_valid())

    def test_login_with_wrong_password(self):
        form = UserLoginForm({
            'username_or_email': 'test@test.com',
            'password': ''
        })
        self.assertFalse(form.is_valid())
        self.assertIn('This field is required.', form.errors['password'])

    def test_registration_form_valid(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'username': 'testperson',
            'password1': 'password',
            'password2': 'password'
        })
        self.assertTrue(form.is_valid())

    def test_registration_form_incomplete(self):
        form = UserRegistrationForm({
            'email': 'test@test.com'
        })

        self.assertIn('This field is required.', form.errors['username'])
        self.assertIn('This field is required.', form.errors['password1'])
        self.assertIn('This field is required.', form.errors['password2'])

    def test_registration_no_password_match(self):
        form = UserRegistrationForm({
            'email': 'test@test.com',
            'username': 'testperson',
            'password1': 'password',
            'password2': 'wrongpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('Passwords do not match', form.errors['password2'])
