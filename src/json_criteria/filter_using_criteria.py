from typing import Dict, Any, List
from .internal import meets_crit

def filter_using_criteria(
    records: List[Dict[str, Any]],
    criteria: Dict[str, Any]
) -> List[Dict[str, Any]]:
    """
    Filter a list of records using the given criteria.

    Parameters:
    - records (List[Dict[str, Any]]): The data records.
    - criteria (Dict[str, Any]): The criteria. Should be a dictionary representing the conditions that the record must satisfy. May include nested conditions.

    Returns:
    - List[Dict[str, Any]]: The filtered records that meet the criteria.
    """
    return [record for record in records if meets_crit(record, criteria)]
