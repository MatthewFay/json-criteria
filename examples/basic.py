from json_criteria import matches_criteria

record = { 'name': 'Joe' , 'age': 30 }
criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
result = matches_criteria(record, criteria)
