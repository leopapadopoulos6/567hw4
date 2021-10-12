import unittest
import json
from unittest import mock
import sys

from requests.models import Response
sys.path.append("/Users/Leo/python/567")
from HW4a import github

class TestHW4a(unittest.TestCase):
    def test_request(self):
        with mock.patch('requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.json.return_value = [
                {'name': '1'},
                {'name': '2'}
            ]
            result = github('leopapadopoulos6')
            self.assertEqual(result, ['Repo: 1 Commit info: 2',
                'Repo: 2 Commit info: 2',])

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
