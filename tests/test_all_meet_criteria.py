import unittest

from src.json_criteria import all_meet_criteria

class TestAllMeetCriteria(unittest.TestCase):
    def test_true(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 30 }
        result = all_meet_criteria(records, criteria)
        self.assertTrue(result)

    def test_false(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
        result = all_meet_criteria(records, criteria)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
