import time
from datetime import datetime


@dataclass
class ModelTime:
    create_time: datetime
    update_time: datetime
