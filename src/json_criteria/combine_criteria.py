from typing import Dict, Any, List, Literal

def combine_criteria(
    operator: Literal['AND', 'OR'],
    criteria_list: List[Dict[str, Any]]
) -> Dict[str, Any]:
    """
    Combine multiple criteria using AND or OR operator.

    Parameters:
    - operator (Literal['AND', 'OR']): The operator to use when combining.
    - criteria_list (List[Dict[str, Any]]): The list of criteria to combine.

    Returns:
    - Dict[str, Any]: The new combined criteria.
    """
    if not criteria_list:
        # Return an empty criteria if the list is empty
        return {}

    # Validate that the operator is either 'AND' or 'OR'
    if operator not in ['AND', 'OR']:
        raise ValueError("Invalid operator. Use 'AND' or 'OR'.")

    # If there is only one criteria, return it directly
    if len(criteria_list) == 1:
        return criteria_list[0]

    # Combine multiple criteria using the specified operator
    return {operator: criteria_list}
