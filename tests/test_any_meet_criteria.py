import unittest

from src.json_criteria import any_meet_criteria

class TestAnyMeetCriteria(unittest.TestCase):
    def test_true(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'name', 'op': 'starts_with', 'value': 'S' }
        result = any_meet_criteria(records, criteria)
        self.assertTrue(result)

    def test_false(self):
        records = [{ 'name': 'Joe' , 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
        criteria = { 'key': 'age', 'op': 'equal_to', 'value': 300 }
        result = any_meet_criteria(records, criteria)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
