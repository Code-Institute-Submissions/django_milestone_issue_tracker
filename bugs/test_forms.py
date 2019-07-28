from django.test import TestCase
from .forms import BugForm, BugCommentForm

# Create your tests here.
class TestBugForm(TestCase):

    # Create Bug
    def test_can_create_bug(self):
        form = BugForm({'name': 'Create Bug', 'description': 'test bug'})
        self.assertTrue(form.is_valid())
        
    def test_correct_message_for_missing_name(self):
        form = BugForm({'name': '', 'description': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
    
    # Comment on bug
    def test_can_create_comment(self):
        form = BugCommentForm({'content': 'test comment'})
        self.assertTrue(form.is_valid())
    
    def test_correct_message_for_missing_comment(self):
        form = BugCommentForm({'content': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['content'], [u'This field is required.'])
    
    