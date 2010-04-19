from silcc.tests import *

class TestApiController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='api', action='index'))
        # Test response...
