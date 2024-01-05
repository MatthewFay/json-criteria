import unittest

from src.json_criteria.internal import meets_crit

class TestMeetsCrit(unittest.TestCase):
    def test_basic(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_basic2(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 30 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Joe' }
            ]
        }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_basic3(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = { 'AND': [
            {'key': 'age', 'op': 'equal_to', 'value': 300 },
            {'key': 'name', 'op': 'equal_to', 'value': 'Joe' }
            ]
        }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_single_cond_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'equal_to', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_single_cond_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'equal_to', 'value': 29 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_AND_true(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'AND': [
            {'key': 'id', 'op': 'equal_to', 'value': 1 },
            {'key': 'email', 'op': 'equal_to', 'value': 'test@email.com' },
            {'key': 'is_active', 'op': 'equal_to', 'value': True }
            ]
        }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_AND_false(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'AND': [
            {'key': 'id', 'op': 'equal_to', 'value': 1 },
            {'key': 'email', 'op': 'equal_to', 'value': 'test@email.com' },
            {'key': 'is_active', 'op': 'equal_to', 'value': False }
            ]
        }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_OR_true(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'OR': [
            {'key': 'id', 'op': 'greater_than', 'value': 1 },
            {'key': 'email', 'op': 'equal_to', 'value': 'test@email.com' },
            ]
        }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_OR_false(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'OR': [
            {'key': 'id', 'op': 'greater_than', 'value': 1 },
            {'key': 'is_active', 'op': 'equal_to', 'value': False },
            ]
        }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_NOT_true(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'NOT': {'key': 'id', 'op': 'greater_than', 'value': 1 } }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_NOT_false(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = { 'NOT': {'key': 'id', 'op': 'greater_than', 'value': 0 } }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_combination_1_true(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = {
            'NOT': {
                'AND': [
                    { 'key': 'id', 'op': 'greater_than', 'value': 1 },
                    { 'key': 'id', 'op': 'less_than', 'value': 0 }
                ]
            }
        }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_combination_1_false(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = {
            'NOT': {
                'AND': [
                    { 'key': 'id', 'op': 'greater_than', 'value': 0 },
                    { 'key': 'id', 'op': 'less_than', 'value': 2 }
                ]
            }
        }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_nested_three_levels(self):
        user_record = {
            'user_type': 1,
            'email': 'test@email.com',
            'is_active': True,
            'age': 30,
            'department': 'Engineering'
        }

        criteria = {
            'AND': [
                {'key': 'user_type', 'op': 'equal_to', 'value': 1},
                {'OR': [
                    {'key': 'email', 'op': 'ends_with', 'value': '@email.com'},
                    {'AND': [
                        {'key': 'is_active', 'op': 'equal_to', 'value': True},
                        {'key': 'age', 'op': 'less_than', 'value': 40}
                    ]}
                ]},
                {'AND': [
                    {'key': 'department', 'op': 'equal_to', 'value': 'Engineering'},
                    {'OR': [
                        {'key': 'is_active', 'op': 'equal_to', 'value': True},
                        {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 30}
                    ]}
                ]},
                {'AND': [
                    {'key': 'user_type', 'op': 'not_equal_to', 'value': 2},
                    {'key': 'email', 'op': 'not_ends_with', 'value': '@test.com'}
                ]}
            ]
        }

        result = meets_crit(user_record, criteria)

        self.assertTrue(result)

    def test_invalid_key(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = {
            'NOT': {
                'AND': [
                    { 'key': 1, 'op': 'greater_than', 'value': 0 },
                    { 'key': 'id', 'op': 'less_than', 'value': 2 }
                ]
            }
        }
        with self.assertRaises(ValueError) as context:
            meets_crit(record, criteria)
        
        self.assertEqual(str(context.exception), 'Invalid condition: {\'key\': 1, \'op\': \'greater_than\', \'value\': 0}')

    def test_invalid_value(self):
        record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }
        criteria = {
            'NOT': {
                'AND': [
                    { 'key': 'id', 'op': 'greater_than', 'value': None },
                    { 'key': 'id', 'op': 'less_than', 'value': 2 }
                ]
            }
        }
        with self.assertRaises(ValueError) as context:
            meets_crit(record, criteria)
        
        self.assertEqual(str(context.exception), 'Invalid condition: {\'key\': \'id\', \'op\': \'greater_than\', \'value\': None}')

    def test_not_equal_to_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'not_equal_to', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_not_equal_to_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'not_equal_to', 'value': 300 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_greater_than_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'greater_than', 'value': 5 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_greater_than_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'greater_than', 'value': 35 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_greater_than_or_equal_to_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_greater_than_or_equal_to_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 31 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_less_than_or_equal_to_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'less_than_or_equal_to', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_less_than_or_equal_to_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'less_than_or_equal_to', 'value': 29 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_less_than_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'less_than', 'value': 31 }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_less_than_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'less_than', 'value': 30 }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

    def test_in_true(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'in', 'value': [28, 29, 30, 31] }
        result = meets_crit(record, criteria)
        self.assertTrue(result)

    def test_in_false(self):
        record = { 'name': 'Joe' , 'age': 30 }
        criteria = {'key': 'age', 'op': 'in', 'value': [28, 29, 31] }
        result = meets_crit(record, criteria)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
