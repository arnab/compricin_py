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
        response = self.client.get(reverse('aggregator:start'))
        self.assertEqual(response.status_code, 200)
