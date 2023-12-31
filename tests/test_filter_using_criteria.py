import unittest

from src.json_criteria import filter_using_criteria

class TestFilterUsingCriteria(unittest.TestCase):
    def test_filter(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'name', 'op': 'starts_with', 'value': 'S' }
        result = filter_using_criteria(records, criteria)
        self.assertListEqual(result, [{ 'name': 'Steve', 'age': 60 }])

if __name__ == '__main__':
    unittest.main()
