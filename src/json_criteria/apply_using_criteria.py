from typing import Dict, Any, List, Callable
from .internal import meets_crit

def apply_using_criteria(
    records: List[Dict[str, Any]],
    criteria: Dict[str, Any],
    func: Callable[[Dict[str, Any]], Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Apply a specified function to each record that meets the given criteria.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.
    - func (Callable): Function to apply to records that meet the criteria.

    Returns:
    - list: List of records with the specified function applied.
    """
    result_records = []
    for record in records:
        if meets_crit(record, criteria):
            result_records.append(func(record))
        else:
            result_records.append(record)
    return result_records
