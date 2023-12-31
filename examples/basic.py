from json_criteria import meets_criteria

record = { 'name': 'Joe' , 'age': 30 }
criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
result = meets_criteria(record, criteria)
