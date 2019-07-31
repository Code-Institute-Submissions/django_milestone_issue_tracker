from django.test import TestCase
from .forms import FeatureForm, FeatureCommentForm


class TestFeatureForm(TestCase):
    def test_can_create_feature(self):
        form = FeatureForm({'name': 'Create Feature',
                           'description': 'test feature'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = FeatureForm({'name': '', 'description': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])

    # Comment on feature
    def test_can_create_comment(self):
        form = FeatureCommentForm({'content': 'test comment'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_comment(self):
        form = FeatureCommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
