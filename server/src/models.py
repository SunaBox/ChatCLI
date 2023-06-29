from typing import List, Optional, Dict
from pydantic import BaseModel


class CLIInput(BaseModel):
    character: Optional[str]
    chat_log: List[Dict[str, str]]


class Response(BaseModel):
    response: str
    command: Optional[str]
