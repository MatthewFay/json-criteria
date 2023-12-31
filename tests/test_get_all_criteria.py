import unittest

from src.json_criteria import get_all_criteria

class TestGetAllCriteria(unittest.TestCase):
    def test_get(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria_list = [
            { 'key': 'name', 'op': 'ends_with', 'value': 've' },
            { 'AND': [{ 'key': 'age', 'op': 'less_than', 'value': 50 }] }
        ]
        result = get_all_criteria(record, criteria_list)
        self.assertEqual(result, [{ 'AND': [{ 'key': 'age', 'op': 'less_than', 'value': 50 }] }])

    def test_get_none(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria_list = [
            { 'key': 'name', 'op': 'ends_with', 'value': 've' },
            { 'AND': [{ 'key': 'age', 'op': 'less_than', 'value': 20 }] }
        ]
        result = get_all_criteria(record, criteria_list)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
