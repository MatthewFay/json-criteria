# json-criteria

`json-criteria` is a lightweight, dependency-free Python library designed for evaluating data against serializable JSON criteria. This library supports multiple operators and nested conditions, providing a flexible and powerful tool for condition-based decision-making.

## Why use `json-criteria`?

* **Serialization to JSON**
  * The criteria used by `json-criteria` can be easily serialized to JSON format. This enables the persistence of criteria, making it suitable for storage in databases or external configurations.
* **Dynamic Criteria Adjustment**
  * Since the criteria is stored as JSON, it allows for dynamic adjustments without the need for code deployment. Criteria can be modified or extended as needed, providing a convenient way to adapt application behavior without code changes.
* **Flexibility and Maintainability**
  * Storing conditions in a serializable format enhances application flexibility and maintainability. Criteria can be fine-tuned, added, or removed independently of the application code, resulting in a more adaptable and easier-to-maintain system.
* **Dependency-Free**
  * `json-criteria` is intentionally designed to be lightweight and dependency-free, ensuring ease of integration into diverse projects without introducing unnecessary dependencies.

In summary, `json-criteria` empowers developers with a versatile and lightweight solution for handling criteria, fostering a more dynamic, adaptable, and maintainable approach to decision-making in applications.

## Examples

### Simple Condition:

Evaluate a single condition using `json_criteria`:

```python
from json_criteria import meets_criteria

# Define a record and criteria
record = {'name': 'Joe', 'age': 30}
criteria = {'key': 'age', 'op': 'equal_to', 'value': 30}

# Check if the record meets the criteria
# `result` will be True
result = meets_criteria(record, criteria)
```

### Nested Conditions:

Handle more complex scenarios with nested conditions:

```python
from json_criteria import meets_criteria

# Define a record and a set of nested conditions
record = {'name': 'Joe', 'age': 30, 'department': 'A13'}

# criteria: age < 40 AND (department starts with 'B' OR department ends with '13')
criteria = {
    'AND': [
        {'key': 'age', 'op': 'less_than', 'value': 40},
        {'OR': [
            {'key': 'department', 'op': 'starts_with', 'value': 'B'},
            {'key': 'department', 'op': 'ends_with', 'value': '13'}
        ]}
    ]
}

# Check if the record meets the criteria
# `result` will be True
result = meets_criteria(record, criteria)
```

These examples demonstrate the simplicity and power of `json_criteria` in handling both basic and intricate conditions for evaluating data. The library's support for nested conditions enables the representation of complex logical structures, making it a valuable tool for decision-making in various scenarios.

## Criteria

Criteria in `json-criteria` are represented as dictionaries, specifying the conditions that record(s) must satisfy. This allows for flexible and expressive criteria, supporting both simple conditions and intricate logical structures with AND, OR, and NOT operators.

Individual conditions are composed of `key`, `op` (operator), and `value`.

Other keys, e.g. `id`, `description`, can be present without issue. This allows flexible addition of relevant information to criteria.

### Operators

The following operators are currently supported:

* equal_to
* not_equal_to
* greater_than
* less_than
* greater_than_or_equal_to
* less_than_or_equal_to
* in
* contains
* starts_with
* ends_with
* matches_regex

These operators provide a comprehensive set of comparisons to handle a wide range of conditions in your criteria.

## API

Below you will find documentation for each library function, including examples.

`all_meet_criteria`: Determine if all of the records meet the given criteria.

```python
records = [{ 'name': 'Joe', 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
criteria = { 'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 30 }

# `result` will be True
result = all_meet_criteria(records, criteria)
```

`any_meet_criteria`: Determine if any of the records meet the given criteria.

```python
records = [{ 'name': 'Joe', 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
criteria = { 'key': 'age', 'op': 'equal_to', 'value': 300 }

# `result` will be False
result = any_meet_criteria(records, criteria)
```

`apply_using_criteria`: Apply a specified function to each record that meets the given criteria.

```python
records = [{ 'name': 'Joe', 'age': 30 }, { 'name': 'John', 'age': 60 }]

criteria = { 'AND': [{ 'key': 'age', 'op': 'less_than', 'value': 50 }] }

def func(record):
    record['is_active'] = True
    return record

# `result` will be:
# [{ 'name': 'Joe', 'age': 30, 'is_active': True }, { 'name': 'John', 'age': 60 }]
result = apply_using_criteria(records, criteria, func)
```

`combine_criteria`: Combine multiple criteria using AND or OR operator.

```python
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

# `result` will be:
# {
#     'AND': [
#         { 'AND': [
#             { 'key': 'name', 'op': 'starts_with', 'value': 'S' }, 
#             { 'key': 'age', 'op': 'equal_to', 'value': 100 }
#             ] 
#         },
#         { 'OR': [
#             { 'key': 'name', 'op': 'starts_with', 'value': 'L' }, 
#             { 'key': 'age', 'op': 'equal_to', 'value': 20 }
#             ]
#         }
#     ]
# }
result = combine_criteria('AND', [criteria1, criteria2])
```

`filter_using_criteria`: Filter a list of records using the given criteria.

```python
records = [{ 'name': 'Joe', 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
criteria = { 'key': 'name', 'op': 'starts_with', 'value': 'S' }

# `result` will be:
# [{ 'name': 'Steve', 'age': 60 }]
result = filter_using_criteria(records, criteria)
```

`find_using_criteria`: Find the first record that meets the given criteria. Returns `None` if none found.

```python
records = [{ 'name': 'Joe', 'age': 30 }, { 'name': 'Steve', 'age': 60 }]
criteria = { 'key': 'name', 'op': 'ends_with', 'value': 've' }

# `result` will be:
# { 'name': 'Steve', 'age': 60 }
result = find_using_criteria(records, criteria)
```

`get_all_criteria`: Given a record and a list of criteria, get all criteria that the record meets.

```python
record = { 'name': 'Joe', 'age': 30 }
criteria_list = [
    { 'id': 1, 'key': 'name', 'op': 'ends_with', 'value': 've' },
    { 'id': 2, 'AND': [
        { 'key': 'age', 'op': 'less_than', 'value': 50 },
        { 'key': 'age', 'op': 'greater_than', 'value': 20 }
        ]
    }
]

# `result` will be:
# [{ 'id': 2, 'AND': [
#     { 'key': 'age', 'op': 'less_than', 'value': 50 },
#     { 'key': 'age', 'op': 'greater_than', 'value': 20 }
#     ]
# }]
result = get_all_criteria(record, criteria_list)
```

`meets_criteria`: Determine if a record meets the given criteria.

```python
record = { 'id': 1 , 'email': 'test@email.com', 'is_active': True }

criteria = { 'AND': [
    {'key': 'id', 'op': 'equal_to', 'value': 1 },
    {'key': 'email', 'op': 'equal_to', 'value': 'test@email.com' },
    {'key': 'is_active', 'op': 'equal_to', 'value': True }
    ]
}

# `result` will be True
result = meets_criteria(record, criteria)
```

## Contributing Guide

I welcome all pull requests. Please make sure you add appropriate test cases for any features added.
