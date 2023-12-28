from typing import Dict, Any

def satisfies_crit(record: Dict[str, Any], element: Dict[str, Any]) -> bool:
    # TODO: `element` validation

    # AND, OR, NOT operators
    if 'AND' in element:
        return all(satisfies_crit(record, el) for el in element.get('AND', []))
    if 'OR' in element:
        return any(satisfies_crit(record, el) for el in element.get('OR', []))
    if 'NOT' in element:
        return not satisfies_crit(record, element.get('NOT', {}))

    # Conditions
    key = element.get('key')
    operator = element.get('op')
    value = element.get('value')

    if not isinstance(key, str):
        raise ValueError(f'Invalid key: {key}')

    if value is None:
        raise ValueError(f'Invalid value: {value}')

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
        return value in record.get(key)

    raise ValueError(f'Invalid operator: {operator}')
