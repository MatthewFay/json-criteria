from typing import Dict, Any

def matches_crit(record: Dict[str, Any], element: Dict[str, Any]) -> bool:
    """
    Internal function to check if a record matches the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - element (Dict[str, Any]): The element of the criteria.

    Returns:
    - bool: Whether or not the record matches the criteria.
    """

    if not isinstance(element, dict):
        raise ValueError('Invalid element: must be a dictionary')

    # AND, OR, NOT operators
    if 'AND' in element:
        return all(matches_crit(record, el) for el in element.get('AND', []))
    if 'OR' in element:
        return any(matches_crit(record, el) for el in element.get('OR', []))
    if 'NOT' in element:
        return not matches_crit(record, element.get('NOT', {}))

    # Conditions
    key = element.get('key')
    operator = element.get('op')
    value = element.get('value')

    if not isinstance(key, str) or not operator or value is None:
        raise ValueError(f'Invalid condition: {element}')

    # Operator conditions
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

    raise ValueError(f'Invalid operator: {operator}')
