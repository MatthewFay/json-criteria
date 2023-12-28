from typing import Dict, Any
from .internal import satisfies_crit

def satisfies_criteria(record: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    return satisfies_crit(record, criteria)
