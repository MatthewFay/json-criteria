import unittest

from src.json_criteria import matches_criteria

class TestMatchesCriteria(unittest.TestCase):
    def test_basic(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
        result = matches_criteria(record, criteria)
        self.assertTrue(result)

    def test_basic2(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 30 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Joe' }
            ]
        }
        result = matches_criteria(record, criteria)
        self.assertTrue(result)

    def test_basic3(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 30 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Steve' }
            ]
        }
        result = matches_criteria(record, criteria)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
