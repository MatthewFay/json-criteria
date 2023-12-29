from typing import Dict, Any
from .internal import matches_crit

def matches_criteria(record: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    """
    Determine if a record matches the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.

    Returns:
    - bool: Whether or not the record matches the criteria.
    """
    return matches_crit(record, criteria)
