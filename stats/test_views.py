from django.test import TestCase


class TestJsonDataViews(TestCase):
    # Test stats page
    def test_stats_page(self):
        response = self.client.get('/stats/')
        self.assertEqual(response.status_code, 200)

    # Testing all JSON data pages
    def test_bugs_status(self):
        response = self.client.get('/stats/get_bug_stats/')
        self.assertEqual(response.status_code, 200)

    def test_features_status(self):
        response = self.client.get('/stats/get_feature_stats/')
        self.assertEqual(response.status_code, 200)

    def test_top_bugs(self):
        response = self.client.get('/stats/top_bugs_stats/')
        self.assertEqual(response.status_code, 200)

    def test_top_features(self):
        response = self.client.get('/stats/top_feature_stats/')
        self.assertEqual(response.status_code, 200)

    def test_features_vs_stats(self):
        response = self.client.get('/stats/bugs_vs_features_stats/')
        self.assertEqual(response.status_code, 200)
