from .model_time import ModelTime
from datetime import datetime


@dataclasses(frozen=True)
class ModelLog:
    id: int
    table_name: str
    target_id: int
    event: str
    content: str
