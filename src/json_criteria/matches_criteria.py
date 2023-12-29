from typing import Dict, Any
from .internal import matches_crit

def matches_criteria(record: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    """
    Determine if a record satisfies the criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - criteria (Dict[str, Any]): The criteria.

    Returns:
    - bool: Whether or not the record satisfies the criteria.
    """
    return matches_crit(record, criteria)
