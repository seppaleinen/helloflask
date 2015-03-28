import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from application import secondView
from tests import unittest


class secondViewTestCase(unittest.TestCase):
    def setUp(self):
        secondView.app.config['TESTING'] = True
        self.app = secondView.app.test_client()

    def tearDown(self):
        self.app = None

    def test_secondView(self):
        result = self.app.get('/test')
        assert 'megasnajs' in result.data