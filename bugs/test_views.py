from django.test import TestCase
from django.contrib.auth.models import User
from .models import Bug


class TestBugViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='username',
                                             password='password')
        self.client.login(username='username', password='password')

    @staticmethod
    def create_test_bug(self):
        bug = Bug(name='Test', description='Test description',
                  author=self.user)
        bug.save()
        return bug

    def test_bugs_page(self):
        response = self.client.get('/bugs/all/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bugs.html')

    def test_bug_detail_page(self):
        bug = self.create_test_bug(self)
        response = self.client.get('/bugs/{}/'.format(bug.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_detail.html')

    def test_bug_report_page(self):
        response = self.client.get('/bugs/bug-report/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bug_request_form.html')

    def test_comment_bug(self):
        bug = self.create_test_bug(self)
        data = {
            'content': 'test comment'
        }
        response = self.client.post('/bugs/{}/'.format(bug.id), data,
                                    follow=True)
        self.assertContains(response, 'You have successfully posted a comment',
                            1, 200)

    def test_upvote_bug(self):
        bug = self.create_test_bug(self)
        response = self.client.post('/bugs/{}/upvote/'.format(bug.id),
                                    follow=True)
        self.assertContains(response, 'Thanks for your vote!', 1, 200)
