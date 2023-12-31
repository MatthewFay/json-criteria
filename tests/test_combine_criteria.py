import unittest

from src.json_criteria import combine_criteria

class TestCombineCriteria(unittest.TestCase):
    def test_combine_and(self):
        criteria1 = { 'key': 'name', 'op': 'starts_with', 'value': 'S' }
        criteria2 = { 'key': 'age', 'op': 'equal_to', 'value': 100 }
        result = combine_criteria('AND', [criteria1, criteria2])
        self.assertDictEqual(result, {
            'AND': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'S' },
                { 'key': 'age', 'op': 'equal_to', 'value': 100 }
            ]
        })

    def test_combine_or(self):
        criteria1 = { 'key': 'name', 'op': 'starts_with', 'value': 'S' }
        criteria2 = { 'key': 'age', 'op': 'equal_to', 'value': 100 }
        result = combine_criteria('OR', [criteria1, criteria2])
        self.assertDictEqual(result, {
            'OR': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'S' },
                { 'key': 'age', 'op': 'equal_to', 'value': 100 }
            ]
        })

    def test_combine_and_2(self):
        criteria1 = {
            'AND': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'S' },
                { 'key': 'age', 'op': 'equal_to', 'value': 100 }
            ]
        }
        criteria2 = {
            'OR': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'L' },
                { 'key': 'age', 'op': 'equal_to', 'value': 20 }
            ]
        }
        result = combine_criteria('AND', [criteria1, criteria2])
        self.assertDictEqual(result, {
            'AND': [
                { 'AND': [{ 'key': 'name', 'op': 'starts_with', 'value': 'S' }, { 'key': 'age', 'op': 'equal_to', 'value': 100 }] },
                { 'OR': [{ 'key': 'name', 'op': 'starts_with', 'value': 'L' }, { 'key': 'age', 'op': 'equal_to', 'value': 20 }] }
            ]
        })

    def test_combine_or_2(self):
        criteria1 = {
            'AND': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'S' },
                { 'key': 'age', 'op': 'equal_to', 'value': 100 }
            ]
        }
        criteria2 = {
            'OR': [
                { 'key': 'name', 'op': 'starts_with', 'value': 'L' },
                { 'key': 'age', 'op': 'equal_to', 'value': 20 }
            ]
        }
        result = combine_criteria('OR', [criteria1, criteria2])
        self.assertDictEqual(result, {
            'OR': [
                { 'AND': [{ 'key': 'name', 'op': 'starts_with', 'value': 'S' }, { 'key': 'age', 'op': 'equal_to', 'value': 100 }] },
                { 'OR': [{ 'key': 'name', 'op': 'starts_with', 'value': 'L' }, { 'key': 'age', 'op': 'equal_to', 'value': 20 }] }
            ]
        })

if __name__ == '__main__':
    unittest.main()
