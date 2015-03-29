import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from application import secondView
from flask import url_for
from tests import unittest, STATUS_405, STATUS_200


class secondViewTestCase(unittest.TestCase):
    def setUp(self):
        secondView.app.config['TESTING'] = True
        self.app = secondView.app.test_client()
        with secondView.app.test_request_context():
            self.url = url_for('tester')

    def tearDown(self):
        self.app = None

    def test_tester_get_allowed(self):
        result = self.app.get(self.url)
        assert STATUS_200 in result.status
        assert 'megasnajs' in result.data

    def test_tester_post_not_allowed(self):
        result = self.app.post(self.url)
        assert STATUS_405 in result.status

    def test_tester_put_not_allowed(self):
        result = self.app.put(self.url)
        assert STATUS_405 in result.status

    def test_tester_delete_not_allowed(self):
        result = self.app.delete(self.url)
        assert STATUS_405 in result.status