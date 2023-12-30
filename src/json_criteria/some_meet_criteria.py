from typing import Dict, Any, List
from .internal import meets_crit

def some_meet_criteria(records: List[Dict[str, Any]], criteria: Dict[str, Any]) -> bool:
    """
    Determine if some of the records meet the given criteria.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.

    Returns:
    - bool: Whether some of the records meet the criteria.
    """
    return any(meets_crit(record, criteria) for record in records)
