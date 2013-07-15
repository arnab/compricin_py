"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

from django.core.urlresolvers import reverse

class AggregatorViewsTest(TestCase):
    def test_search_view_renders(self):
        """
        Can successfully get to the (main) entry-point view
        """
        response = self.client.get(reverse('aggregator:search'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Search for")
        self.assertContains(response, "In these stores")

    def test_validate_empty_query_string(self):
        """
        If the query string is empty, a validation error should be shown
        """
        response = self.client.get(reverse('aggregator:search'), {'q': ''})
        self.assertContains(response, "Please enter something to search for")

    def test_search_should_only_accept_safe_methods(self):
        """
        Everything except GET/HEAD should be rejected
        """
        search_url = reverse('aggregator:search')
        for method in ['post', 'put', 'delete']:
            response = getattr(self.client, method)(search_url)
            self.assertEqual(response.status_code, 405)
