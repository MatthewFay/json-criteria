from typing import Dict, Any, List
from .internal import meets_crit

def find_using_criteria(
    records: List[Dict[str, Any]],
    criteria: Dict[str, Any]
) -> Dict[str, Any] | None:
    """
    Find the first record that meets the given criteria. Returns `None` if none found.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.

    Returns:
    - Dict[str, Any] | None: The first record that meets the criteria, otherwise None.
    """
    return next((record for record in records if meets_crit(record, criteria)), None)
