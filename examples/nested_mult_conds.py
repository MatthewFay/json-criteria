from json_criteria import meets_criteria

record = { 'name': 'Joe', 'age': 30, 'department': 'A13' }

# age < 40 AND (department starts with 'B' OR department ends with '13')
criteria = {
    'AND': [
        { 'key': 'age', 'op': 'less_than', 'value': 40 },
        { 'OR': [
            { 'key': 'department', 'op': 'starts_with', 'value': 'B' },
            { 'key': 'department', 'op': 'ends_with', 'value': '13' }
        ]},
    ]
}

# `result` will be True
result = meets_criteria(record, criteria)
