from typing import Dict, Any
from .internal import meets_crit

def meets_criteria(record: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    """
    Determine if a record meets the given criteria.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.

    Returns:
    - bool: Whether or not the record meets the criteria.
    """
    return meets_crit(record, criteria)
