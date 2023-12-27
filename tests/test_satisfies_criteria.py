import unittest

from src.json_criteria import satisfies_criteria

class TestSatisfiesCriteria(unittest.TestCase):
    def test_basic(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'key': 'age', 'op': 'equals', 'value': 30 }
        result = satisfies_criteria(record, criteria)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
