import unittest

from src.json_criteria import find_using_criteria

class TestFindUsingCriteria(unittest.TestCase):
    def test_find(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'name', 'op': 'ends_with', 'value': 've' }
        result = find_using_criteria(records, criteria)
        self.assertEqual(result, { 'name': 'Steve', 'age': 60 })

    def test_find_none_found(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'name', 'op': 'in', 'value': ['John'] }
        result = find_using_criteria(records, criteria)
        self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()
