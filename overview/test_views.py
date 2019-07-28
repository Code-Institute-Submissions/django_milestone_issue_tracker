from django.test import TestCase
from django.shortcuts import get_object_or_404

class TestOverviewViews(TestCase):
    # Test overview page
    def test_overview_page(self):
        response = self.client.get('/overview/')
        self.assertEqual(response.status_code, 200)
