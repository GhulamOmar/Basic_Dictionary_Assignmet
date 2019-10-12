import unittest
from more_fun_with_collections import dict_membership


class ScoreTestCase(unittest.TestCase):
    def test_in_dict(self):
        """ tests false is true"""
        name = 'score1'
        expected_result = {'score': 50}
        self.assertFalse(expected_result.get(name))

    def test_in_dict_is_true(self):
        name = 'score3'
        expected_result = {'score3': 50}
        self.assertTrue(expected_result.get(name))


if __name__ == '__main__':
    unittest.main()
