import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from application import commandView
from tests import unittest
from flask import url_for

class commandViewTestCase_removeTorrent(unittest.TestCase):
    def setUp(self):
        commandView.app.config['TESTING'] = True
        self.app = commandView.app.test_client()
        with commandView.app.test_request_context():
            self.url = url_for('remove_torrent')

    def tearDown(self):
        self.app = None

    def test_put_not_allowed(self):
        result = self.app.put(self.url)
        assert '405' in result.status

    def test_get_not_allowed(self):
        result = self.app.get(self.url)
        assert '405' in result.status

    def test_delete_not_allowed(self):
        result = self.app.delete(self.url)
        assert '405' in result.status

    def test_post_allowed(self):
        result = self.app.post(self.url)
        assert '200' in result.status
        assert '*.torrent' in result.data


class commandViewTestCase_removeTrash(unittest.TestCase):
    def setUp(self):
        commandView.app.config['TESTING'] = True
        self.app = commandView.app.test_client()
        with commandView.app.test_request_context():
            self.url = url_for('remove_trash')

    def tearDown(self):
        self.app = None

    def test_put_not_allowed(self):
        result = self.app.put(self.url)
        assert '405' in result.status

    def test_get_not_allowed(self):
        result = self.app.get(self.url)
        assert '405' in result.status

    def test_delete_not_allowed(self):
        result = self.app.delete(self.url)
        assert '405' in result.status

    def test_post_allowed(self):
        result = self.app.post(self.url)
        assert '200' in result.status
        assert '.Trash' in result.data

class commandViewTestCase_updateGit(unittest.TestCase):
    def setUp(self):
        commandView.app.config['TESTING'] = True
        self.app = commandView.app.test_client()
        with commandView.app.test_request_context():
            self.url = url_for('update_git')

    def tearDown(self):
        self.app = None

    def test_put_not_allowed(self):
        result = self.app.put(self.url)
        assert '405' in result.status

    def test_get_not_allowed(self):
        result = self.app.get(self.url)
        assert '405' in result.status

    def test_delete_not_allowed(self):
        result = self.app.delete(self.url)
        assert '405' in result.status

    def test_post_allowed(self):
        result = self.app.post(self.url)
        assert '200' in result.status
        assert 'git' in result.data