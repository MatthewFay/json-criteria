from typing import Dict, Any

def satisfies_criteria(record: Dict[str, Any], element: Dict[str, Any]) -> bool:
    # TODO: `element` validation

    # AND, OR, NOT operators
    if 'AND' in element:
        return all(satisfies_criteria(record, el) for el in element.get('AND', []))
    if 'OR' in element:
        return any(satisfies_criteria(record, el) for el in element.get('OR', []))
    if 'NOT' in element:
        return not satisfies_criteria(record, element.get('NOT', {}))

    # Conditions
    key = element.get('key')
    operator = element.get('op')
    value = element.get('value')

    if not isinstance(key, str):
        raise ValueError(f'Invalid key: {key}')

    if operator == 'equals':
        return record.get(key) == value

    raise ValueError(f'Invalid operator: {operator}')
