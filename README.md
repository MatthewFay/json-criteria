# json-criteria

`json-criteria` is a small, dependency-free Python library that evaluates data records against easily serializable JSON criteria that support multiple operators, and can include nested conditions.

*Why use `json-criteria`?*

Because the criteria is serializable to JSON, it can be persisted, e.g., in a database, and used by applications to make decisions. If required, criteria can be changed without needing to deploy new code.

## Examples

Here is a simple example with just a single condition.

```python
from json_criteria import meets_criteria

record = { 'name': 'Joe', 'age': 30 }
criteria = { 'key': 'age', 'op': 'equal_to', 'value': 30 }

# `result` will be True
result = meets_criteria(record, criteria)
```

Here is a more complex example with nested conditions.

```python
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
```

## Criteria

Criteria should be a dictionary representing the conditions that the record(s) must satisfy. May include nested conditions, using AND, OR, and NOT operators.

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

## API

Below you will find documentation for each library function, including examples.

`all_meet_criteria`: Determine if all of the records meet the given criteria.

```python
# add
```

`any_meet_criteria`: Determine if any of the records meet the given criteria.

```python
# add
```

`combine_criteria`: Combine multiple criteria using AND or OR operator.

```python
# add
```

`filter_using_criteria`: Filter a list of records using the given criteria.

```python
# add
```

`find_using_criteria`: Find the first record that meets the given criteria. Returns `None` if none found.

```python
# add
```

`get_all_criteria`: Given a record and a list of criteria, get all criteria that the record meets.

```python
# add
```

`map_using_criteria`: Apply a specified function to each record that meets the given criteria.

```python
# add
```

`meets_criteria`: Determine if a record meets the given criteria.

```python
# add
```

## Contributing Guide

I welcome all pull requests. Please make sure you add appropriate test cases for any features added.
