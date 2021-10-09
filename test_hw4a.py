import unittest
from HW4a import github


class TestHW4a(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(github('leopapadopoulos6'), ['Repo: 567hw4 Commit info: 1',
                                                 'Repo: hw01testingtriangles Commit info: 1',
                                                 'Repo: hw01testingtriangles Commit info: 1',
                                                 'Repo: p3-lpapadopoulos Commit info: 1',
                                                 'Repo: ssw567 Commit info: 2',
                                                 'Repo: Triangle567 Commit info: 11'])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
