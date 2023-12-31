from typing import Dict, Any, List
from .internal import meets_crit

def get_all_criteria(
    record: Dict[str, Any],
    criteria_list: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Given a record and a list of criteria, get all criteria that the record meets.

    Parameters:
    - record (Dict[str, Any]): The data record.
    - criteria_list (List[Dict[str, Any]]): The list of criteria to check against.

    Returns:
    - List[Dict[str, Any]]: The list of criteria that the record meets.
    """
    return [criteria for criteria in criteria_list if meets_crit(record, criteria)]
