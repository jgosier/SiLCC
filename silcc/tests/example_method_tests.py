"""Tests the example API method which allows a user to create a pre-tagged example"""
import unittest
import silcc.client
from urllib2 import HTTPError

URLBASE = 'http://127.0.0.1:5002/api/tag/example'

class ExampleTests(unittest.TestCase):
    """
    Test cases for the example API method
    """

    def test_post_an_example(self):
        """
        Test posting a single example to the database through the API.
        """
        silcc.client.example(
            text="This is an example of user feedback",
            key="AAAABBBB",
            tags="example,feedback",
            corpus="unittests",
            urlbase=URLBASE)
            
if __name__ == '__main__':
    unittest.main()
