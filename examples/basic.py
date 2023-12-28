from json_criteria import satisfies_criteria

record = { 'name': 'Joe' , 'age': 30 }
criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }
result = satisfies_criteria(record, criteria)
