"""Tests the various combinations of apicalls with and without keys"""
import unittest
import silcc.client
from urllib2 import HTTPError

URLBASE = 'http://127.0.0.1:5002/api/tag'
TEXT = "this is the text to be tagged"

class TestMultipleCallsWithKey(unittest.TestCase):
    """
    Tests keys that have '*' provided as valid domains.
    (* means that this key is valid for any host)
    Multiple calls in quick succession to make sure the throttling works,
    test with a key which has calls_per_minute set to 60
    """
    def setUp(self):
        """
        Set the key to use, make sure this key exists
        and has a throttle(calls_per_minute) value of 120.
        """
        self.KEY = "AAAABBBB"

    def test_key_with_open_domain(self):
        """
        Test calls to a key with open domains 
        ie valid from all hosts.
        """
        for i in range(0, 120):
            silcc.client.tag(text=TEXT, key=self.KEY, urlbase=URLBASE)
        # The first 120 calls above should go through, the following should 
        # raise HTTPError because of the throttling
        self.assertRaises(HTTPError, silcc.client.tag, 
                          text=TEXT, key=self.KEY, urlbase=URLBASE)
        
class TestKeylessMultiple(unittest.TestCase):
    """
    Tests keyless calls. allow_keyless_calls must be set to
    true in the servers .ini file for this test to pass.
    The first 60 should pass and the final call should fail
    if the throttling is working correctly.
    """

    def test_keyless_call_multiple(self):
        """
        Keyless calls are throttled by ip address.
        This allows any user to use SilCC without a key.
        This is useful for example for the Wordpress plugin.
        Keyless calls are throttled at 60 a minute.
        """
        for i in range(0, 60):
            silcc.client.tag(text=TEXT, key=None, urlbase=URLBASE)
        # The first 60 calls above should go through, the following should 
        # raise HTTPError because of the throttling
        self.assertRaises(HTTPError, silcc.client.tag, 
                          text=TEXT, key=None, urlbase=URLBASE)

class TestInvalidKey(unittest.TestCase):
    """
    Test a call with an invalid key.
    """

    def test_invalid_key(self):
        """Invalid keys should always error"""
        self.assertRaises(HTTPError, silcc.client.tag, 
                          text=TEXT, key='invalid key!', urlbase=URLBASE)

            
if __name__ == '__main__':
    unittest.main()
