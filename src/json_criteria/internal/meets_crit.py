from typing import Dict, Any
# from datetime import datetime
import re

def meets_crit(record: Dict[str, Any], element: Dict[str, Any]) -> bool:
    """
    Internal function to check if a record meets the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - element (Dict[str, Any]): The element of the criteria.

    Returns:
    - bool: Whether or not the record meets the criteria.
    """

    if not isinstance(element, dict):
        raise ValueError('Invalid element: must be a dictionary')

    # AND, OR, NOT operators
    if 'AND' in element:
        return all(meets_crit(record, el) for el in element.get('AND', []))
    if 'OR' in element:
        return any(meets_crit(record, el) for el in element.get('OR', []))
    if 'NOT' in element:
        return not meets_crit(record, element.get('NOT', {}))

    # Conditions
    key = element.get('key')
    operator = element.get('op')
    value = element.get('value')

    if not isinstance(key, str) or not operator or value is None:
        raise ValueError(f'Invalid condition: {element}')

    # Operator conditions - WIP
    # Change to dictionary where key is operator, value is compare function,
    # and break out into another module.
    if operator == 'equal_to':
        return record.get(key) == value
    if operator == 'not_equal_to':
        return record.get(key) != value
    if operator == 'greater_than':
        return record.get(key) > value
    if operator == 'less_than':
        return record.get(key) < value
    if operator == 'greater_than_or_equal_to':
        return record.get(key) >= value
    if operator == 'less_than_or_equal_to':
        return record.get(key) <= value
    if operator == 'in':
        return record.get(key) in value
    if operator == 'not_in':
        return record.get(key) not in value
    if operator == 'contains':
        return value in record.get(key)
    if operator == 'not_contains':
        return value not in record.get(key)
    if operator == 'starts_with':
        return record.get(key, '').startswith(value)
    if operator == 'not_starts_with':
        return not record.get(key, '').startswith(value)
    if operator == 'ends_with':
        return record.get(key, '').endswith(value)
    if operator == 'not_ends_with':
        return not record.get(key, '').endswith(value)
    # if operator == 'is_empty':
    #     return not bool(record.get(key))
    # if operator == 'is_not_empty':
    #     return bool(record.get(key))
    # if operator == 'is_true':
    #     return bool(record.get(key))
    # if operator == 'is_false':
    #     return not bool(record.get(key))
    # if operator == 'is_null':
    #     return record.get(key) is None
    # if operator == 'is_not_null':
    #     return record.get(key) is not None
    if operator == 'matches_regex':
        return re.search(value, str(record.get(key))) is not None
    # if operator == 'equals_ignore_case':
    #     return record.get(key, '').lower() == value.lower()
    # if operator == 'not_equals_ignore_case':
    #     return record.get(key, '').lower() != value.lower()
    # if operator == 'is_date':
    #     try:
    #         parsed_date = datetime.strptime(record.get(key, ''), '%Y-%m-%d')
    #         return True
    #     except ValueError:
    #         return False
    # if operator == 'date_equal_to':
    #     try:
    #         parsed_date = datetime.strptime(record.get(key, ''), '%Y-%m-%d')
    #         return parsed_date == value
    #     except ValueError:
    #         return False
    # if operator == 'date_before':
    #     try:
    #         parsed_date = datetime.strptime(record.get(key, ''), '%Y-%m-%d')
    #         return parsed_date < value
    #     except ValueError:
    #         return False
    # if operator == 'date_after':
    #     try:
    #         parsed_date = datetime.strptime(record.get(key, ''), '%Y-%m-%d')
    #         return parsed_date > value
    #     except ValueError:
    #         return False

    raise ValueError(f'Invalid operator: {operator}')
