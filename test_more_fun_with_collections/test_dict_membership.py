import unittest
from more_fun_with_collections import dict_membership


class ScoreTestCase(unittest.TestCase):
    def test_score_input_test_name(self):
        name = 'test'
        expected_result = {'testeeee':50}
        self.assertFalse(expected_result.get(name))
    def test_score_input_test_name55(self):
        name = 'test'
        expected_result = {'test':50}
        self.assertTrue(expected_result.get(name))


if __name__ == '__main__':
    unittest.main()
