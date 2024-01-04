# json-criteria

`json-criteria` is a lightweight, dependency-free Python library designed for evaluating data against serializable JSON criteria. This library supports multiple operators and nested conditions, providing a flexible and powerful tool for condition-based decision-making.

## Why use `json-criteria`?

* **Serialization to JSON**
  * The criteria used by `json-criteria` can be easily serialized to JSON format. This enables the persistence of criteria, making it suitable for storage in databases or external configurations.
* **Dynamic Criteria Adjustment**
  * Since the criteria is stored as JSON, it allows for dynamic adjustments without the need for code deployment. Criteria can be modified or extended as needed, providing the ability to adapt application behavior without code changes.
* **Flexibility and Maintainability**
  * Storing conditions in a serializable format enhances application flexibility and maintainability. Criteria can be fine-tuned, added, or removed independently of the application code, resulting in a more adaptable and easier-to-maintain system.
* **Dependency-Free**
  * `json-criteria` is intentionally designed to be lightweight and dependency-free, ensuring ease of integration into diverse projects without introducing unnecessary dependencies.

In summary, `json-criteria` empowers developers with a versatile and lightweight solution for handling criteria, fostering a more dynamic, adaptable, and maintainable approach to decision-making in applications.

## Examples

### Simple Condition

Evaluate a single condition:

```python
from json_criteria import meets_criteria

# Define a record and criteria
record = {'name': 'Joe', 'age': 30}
criteria = {'key': 'age', 'op': 'equal_to', 'value': 30}

# Check if the record meets the criteria
# `result` will be True
result = meets_criteria(record, criteria)
```

### Nested Conditions

Handle more complex scenarios with nested conditions:

```python
from json_criteria import meets_criteria

# Define a record
record = {
    'name': 'Alice',
    'age': 28,
    'department': 'Engineering',
    'experience_years': 5,
    'is_manager': False
}

# criteria:
# (age >= 25 AND experience_years >= 3) OR (department is 'Engineering' AND is_manager is True)
criteria = {
    'OR': [
        {'AND': [
            {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 25},
            {'key': 'experience_years', 'op': 'greater_than_or_equal_to', 'value': 3}
        ]},
        {'AND': [
            {'key': 'department', 'op': 'equals', 'value': 'Engineering'},
            {'key': 'is_manager', 'op': 'equals', 'value': True}
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

A condition is composed of three fundamental components:

* `key`: The key to be evaluated.
* `op`: The operator indicating the comparison type.
* `value`: The expected value for the specified key.

Additional keys, such as `id` and `description`, can be included without impacting functionality. This feature provides the flexibility to add context or relevant information to the criteria.

### Supported Operators:

* `equal_to`
* `not_equal_to`
* `greater_than`
* `less_than`
* `greater_than_or_equal_to`
* `less_than_or_equal_to`
* `in`
* `not_in`
* `contains`
* `not_contains`
* `starts_with`
* `not_starts_with`
* `ends_with`
* `not_ends_with`
* `matches_regex`

These operators provide a comprehensive set of comparisons to handle a wide range of conditions in your criteria.

## API

Below you will find documentation for each library function, including examples.

### `all_meet_criteria`

Determine if all records in a given list meet the specified criteria. This function evaluates whether all records in the provided list satisfy the specified criteria, providing a straightforward way to ensure that the entire dataset meets the required conditions.

```python
from json_criteria import all_meet_criteria

# Define a list of user records
user_records = [
    {'name': 'Alice', 'age': 28, 'department': 'Engineering', 'is_manager': False},
    {'name': 'Bob', 'age': 35, 'department': 'Marketing', 'is_manager': True},
    {'name': 'Charlie', 'age': 45, 'department': 'Sales', 'is_manager': False}
]

# criteria: age >= 25 AND (is_manager is True OR department is 'Engineering')
criteria = {
    'AND': [
        {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 25},
        {'OR': [
            {'key': 'is_manager', 'op': 'equals', 'value': True},
            {'key': 'department', 'op': 'equals', 'value': 'Engineering'}
        ]}
    ]
}

# Check if all user records meet the criteria
# `result` will be True
result = all_meet_criteria(user_records, criteria)
```

### `any_meet_criteria`

This function determines whether any record in the provided list satisfies the specified criteria, offering a convenient way to identify if at least one record meets the required conditions.

```python
from json_criteria import any_meet_criteria

# Define a list of employee records and a criteria
employee_records = [
    {'name': 'Alice', 'age': 32, 'department': 'Sales'},
    {'name': 'Bob', 'age': 45, 'department': 'Marketing'},
    {'name': 'Charlie', 'age': 28, 'department': 'Engineering'},
    {'name': 'David', 'age': 37, 'department': 'Sales'},
]

# criteria: age greater than 35 OR (department is 'Engineering' AND age is less than 30)
criteria = {
    'OR': [
        {'key': 'age', 'op': 'greater_than', 'value': 35},
        {'AND': [
            {'key': 'department', 'op': 'equal_to', 'value': 'Engineering'},
            {'key': 'age', 'op': 'less_than', 'value': 30}
        ]}
    ]
}

# Check if any employee record meets the criteria
# `result` will be True
result = any_meet_criteria(employee_records, criteria)
```

### `apply_using_criteria`

Apply a specified function to each record that meets the given criteria. This function allows for targeted and conditional transformations on a list of records, enhancing flexibility in data manipulation.

```python
from json_criteria import apply_using_criteria

# Define a list of user records and a criteria
user_records = [
    {'name': 'Joe', 'age': 30, 'department': 'Sales'},
    {'name': 'John', 'age': 60, 'department': 'Marketing'},
    {'name': 'Alice', 'age': 25, 'department': 'Engineering'},
]

# criteria: Apply the function to records where age is less than 40 AND belong to the 'Engineering' department
criteria = {
    'AND': [
        {'key': 'age', 'op': 'less_than', 'value': 40},
        {'key': 'department', 'op': 'equal_to', 'value': 'Engineering'}
    ]
}

# Define a function to apply (e.g., mark users as active)
def mark_as_active(record):
    record['is_active'] = True
    return record

# Apply the specified function to records meeting the criteria
# `result` will be:
# [{'name': 'Joe', 'age': 30, 'department': 'Sales'},
#  {'name': 'John', 'age': 60, 'department': 'Marketing'},
#  {'name': 'Alice', 'age': 25, 'department': 'Engineering', 'is_active': True}]
result = apply_using_criteria(user_records, criteria, mark_as_active)
```

### `combine_criteria`

Combine multiple criteria using the AND or OR operator. This function allows for the composition of more complex logical conditions by nesting individual criteria within a larger structure.

```python
from json_criteria import combine_criteria

# Define two individual criteria
criteria1 = {
    'AND': [
        {'key': 'name', 'op': 'starts_with', 'value': 'S'},
        {'key': 'age', 'op': 'equal_to', 'value': 100}
    ]
}

criteria2 = {
    'OR': [
        {'key': 'name', 'op': 'starts_with', 'value': 'L'},
        {'key': 'age', 'op': 'equal_to', 'value': 20}
    ]
}

# Combine criteria using the AND operator
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

### `filter_using_criteria`

Filter a list of records based on the given criteria. This function provides a powerful mechanism for selectively extracting records that meet specific conditions, enhancing the flexibility of data filtering.

```python
from json_criteria import filter_using_criteria

# Define a list of employee records
employee_records = [
    {'name': 'Alice', 'age': 28, 'department': 'Engineering', 'is_manager': False},
    {'name': 'Bob', 'age': 35, 'department': 'Marketing', 'is_manager': True},
    {'name': 'Charlie', 'age': 45, 'department': 'Sales', 'is_manager': False},
    {'name': 'Susan', 'age': 30, 'department': 'Engineering', 'is_manager': True}
]

# criteria: (age >= 30 AND is_manager is True) OR (department is 'Engineering' AND name starts with 'S')
criteria = {
    'OR': [
        {'AND': [
            {'key': 'age', 'op': 'greater_than_or_equal_to', 'value': 30},
            {'key': 'is_manager', 'op': 'equals', 'value': True}
        ]},
        {'AND': [
            {'key': 'department', 'op': 'equals', 'value': 'Engineering'},
            {'key': 'name', 'op': 'starts_with', 'value': 'S'}
        ]}
    ]
}

# Filter employee records based on the criteria
# `result` will be: [
#    {'name': 'Bob', 'age': 35, 'department': 'Marketing', 'is_manager': True},
#    {'name': 'Susan', 'age': 30, 'department': 'Engineering', 'is_manager': True}
# ]
result = filter_using_criteria(employee_records, criteria)
```

### `find_using_criteria`

Find the first record that meets the given criteria. Returns `None` if none is found. This function provides a convenient way to locate the initial occurrence of a record satisfying specific conditions within a list.

```python
from json_criteria import find_using_criteria

# Define a list of employee records
employee_records = [
    {'name': 'Alice', 'age': 28, 'department': 'Engineering', 'is_manager': False},
    {'name': 'Bob', 'age': 35, 'department': 'Marketing', 'is_manager': True},
    {'name': 'Charlie', 'age': 45, 'department': 'Sales', 'is_manager': False},
    {'name': 'Susan', 'age': 30, 'department': 'Engineering', 'is_manager': True}
]

# criteria: Find the first employee who is a manager and older than 30
criteria = {'AND': [
    {'key': 'is_manager', 'op': 'equals', 'value': True},
    {'key': 'age', 'op': 'greater_than', 'value': 30}
]}

# Find the first employee record meeting the criteria
# `result` will be: {'name': 'Bob', 'age': 35, 'department': 'Marketing', 'is_manager': True}
result = find_using_criteria(employee_records, criteria)
```

### `get_all_criteria`

Given a record and a list of criteria, retrieve all criteria that the record meets. This function is useful for analyzing and identifying the specific criteria that a record satisfies within a given list.

```python
from json_criteria import get_all_criteria

# Define a user
user = {
    'name': 'Alice',
    'age': 28,
    'interests': ['Technology', 'Books'],
    'purchased_products': ['Laptop']
}

# criteria list:
criteria_list = [
    # User has an interest in 'Technology' AND (User is older than 25 OR User has purchased a 'Laptop')
    {'id': 10, 'AND': [
        {'key': 'interests', 'op': 'contains', 'value': 'Technology'},
        {'OR': [
            {'key': 'age', 'op': 'greater_than', 'value': 25},
            {'key': 'purchased_products', 'op': 'contains', 'value': 'Laptop'}
        ]}
    ]},
    # User has an interest in 'Books' AND User has not purchased a 'Tablet'
    {'id': 11, 'AND': [
        {'key': 'interests', 'op': 'contains', 'value': 'Books'},
        {'key': 'purchased_products', 'op': 'not_contains', 'value': 'Tablet'}
    ]}
]

# Get all criteria that the user meets
# `result` will be:
# [{'id': 10, 'AND': [
#     {'key': 'interests', 'op': 'contains', 'value': 'Technology'},
#     {'OR': [
#         {'key': 'age', 'op': 'greater_than', 'value': 25},
#         {'key': 'purchased_products', 'op': 'contains', 'value': 'Laptop'}
#     ]}
# ]}]
result = get_all_criteria(user, criteria_list)
```

### `meets_criteria`

Determine if a record meets the given criteria. This function provides a flexible and expressive way to evaluate whether a record satisfies specified conditions, supporting a variety of operators for comprehensive criteria checks.

```python
from json_criteria import meets_criteria

# Define a record for a user
user_record = {
    'user_type': 1,
    'email': 'test@email.com',
    'is_active': True,
    'age': 30,
    'department': 'Engineering'
}

# Criteria Description:
# - User type is 1
# - AND (Email ends with '@email.com' OR (Is active AND Age is less than 40))
# - AND (Department is 'Engineering' AND (Is active OR Age is greater than or equal to 30))
# - AND (User type is not 2 AND Email does not end with '@test.com')
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

# Check if the user record meets the specified criteria
# `result` will be True
result = meets_criteria(user_record, criteria)
```

## Contributing Guide

I welcome all pull requests. Please make sure you add appropriate test cases for any features added.
