import unittest

from src.json_criteria import apply_using_criteria

class TestApplyUsingCriteria(unittest.TestCase):
    def test_apply(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'John' , 'age': 60 }]
        criteria = { 'AND': [{ 'key': 'age', 'op': 'less_than', 'value': 50 }] }
        def func(record):
            record['is_active'] = True
            return record
        result = apply_using_criteria(records, criteria, func )
        self.assertEqual(result, [{ 'name': 'Joe' , 'age': 30, 'is_active': True }, { 'name': 'John' , 'age': 60 }])

if __name__ == '__main__':
    unittest.main()
