import unittest

from src.json_criteria.internal import compare

class TestCompare(unittest.TestCase):
    def test_equal_to_true(self):
        result = compare(1, 'equal_to', 1)
        self.assertTrue(result)

    def test_equal_to_false(self):
        result = compare(1, 'equal_to', 2)
        self.assertFalse(result)

    def test_not_equal_to_true(self):
        result = compare(1, 'not_equal_to', 2)
        self.assertTrue(result)

    def test_not_equal_to_false(self):
        result = compare(1, 'not_equal_to', 1)
        self.assertFalse(result)

    def test_in_true(self):
        result = compare('Test', 'in', ['Test'])
        self.assertTrue(result)

    def test_in_false(self):
        result = compare('Test', 'in', ['Test2'])
        self.assertFalse(result)

    def test_not_in_true(self):
        result = compare('Test', 'not_in', ['abc'])
        self.assertTrue(result)

    def test_not_in_false(self):
        result = compare('Test', 'not_in', ['Test'])
        self.assertFalse(result)

    def test_contains_true(self):
        result = compare('[Test]', 'contains', 'Test')
        self.assertTrue(result)

    def test_contains_false(self):
        result = compare('[Test]', 'contains', 'Test2')
        self.assertFalse(result)

    def test_not_contains_true(self):
        result = compare('[Test]', 'not_contains', 'Hello')
        self.assertTrue(result)

    def test_not_contains_false(self):
        result = compare('[Test]', 'not_contains', 'Test')
        self.assertFalse(result)

    def test_matches_regex_true(self):
        result = compare('Hello World', 'matches_regex', '^[a-zA-Z]*\\s[a-zA-Z]*$')
        self.assertTrue(result)

    def test_matches_regex_false(self):
        result = compare('Hello World', 'matches_regex', '^[A-Z]*\\s[A-Z]*$')
        self.assertFalse(result)

    def test_unsupported_operator(self):
        with self.assertRaises(ValueError) as context:
            compare(1, 'unsupported', 1)
        
        self.assertEqual(str(context.exception), 'Unsupported operator: unsupported')

if __name__ == '__main__':
    unittest.main()
