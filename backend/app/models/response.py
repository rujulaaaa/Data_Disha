from pydantic import BaseModel
from typing import Any, Dict, List

class QueryResponse(BaseModel):
    output: List[Dict[str, Any]]
    metadata: Dict[str, Any]