from typing import Any
import re

def compare_equal_to(record_value: Any, value: Any) -> bool:
    """Check if the record value is equal to the specified value."""
    return record_value == value

def compare_not_equal_to(record_value: Any, value: Any) -> bool:
    """Check if the record value is not equal to the specified value."""
    return record_value != value

def compare_greater_than(record_value: Any, value: Any) -> bool:
    """Check if the record value is greater than the specified value."""
    return record_value > value

def compare_less_than(record_value: Any, value: Any) -> bool:
    """Check if the record value is less than the specified value."""
    return record_value < value

def compare_greater_than_or_equal_to(record_value: Any, value: Any) -> bool:
    """Check if the record value is greater than or equal to the specified value."""
    return record_value >= value

def compare_less_than_or_equal_to(record_value: Any, value: Any) -> bool:
    """Check if the record value is less than or equal to the specified value."""
    return record_value <= value

def compare_in(record_value: Any, value: Any) -> bool:
    """Check if the record value is in the specified value."""
    return record_value in value

def compare_not_in(record_value: Any, value: Any) -> bool:
    """Check if the record value is not in the specified value."""
    return record_value not in value

def compare_contains(record_value: Any, value: Any) -> bool:
    """Check if the record value contains the specified value."""
    return value in record_value

def compare_not_contains(record_value: Any, value: Any) -> bool:
    """Check if the record value does not contain the specified value."""
    return value not in record_value

def compare_starts_with(record_value: str, value: Any) -> bool:
    """Check if the record value starts with the specified value."""
    return record_value.startswith(value)

def compare_not_starts_with(record_value: str, value: Any) -> bool:
    """Check if the record value does not start with the specified value."""
    return not record_value.startswith(value)

def compare_ends_with(record_value: str, value: Any) -> bool:
    """Check if the record value ends with the specified value."""
    return record_value.endswith(value)

def compare_not_ends_with(record_value: str, value: Any) -> bool:
    """Check if the record value does not end with the specified value."""
    return not record_value.endswith(value)

def compare_matches_regex(record_value: Any, value: Any) -> bool:
    """Check if the record value matches the specified regex value."""
    return re.search(value, str(record_value)) is not None

operator_functions = {
    'equal_to': compare_equal_to,
    'not_equal_to': compare_not_equal_to,
    'greater_than': compare_greater_than,
    'less_than': compare_less_than,
    'greater_than_or_equal_to': compare_greater_than_or_equal_to,
    'less_than_or_equal_to': compare_less_than_or_equal_to,
    'in': compare_in,
    'not_in': compare_not_in,
    'contains': compare_contains,
    'not_contains': compare_not_contains,
    'starts_with': compare_starts_with,
    'not_starts_with': compare_not_starts_with,
    'ends_with': compare_ends_with,
    'not_ends_with': compare_not_ends_with,
    'matches_regex': compare_matches_regex
}

def compare(record_value: Any, operator: str, value: Any) -> bool:
    """
    Compare record value with the specified value using the given operator.

    Parameters:
    - record_value (Any): The value from the data record.
    - operator (str): The comparison operator.
    - value (Any): The value to compare against.

    Returns:
    - bool: The result of the comparison.
    """

    if operator in operator_functions:
        return operator_functions[operator](record_value, value)

    raise ValueError(f"Unsupported operator: {operator}")
