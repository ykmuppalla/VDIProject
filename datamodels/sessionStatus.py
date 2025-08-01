from enum import Enum
class SessionStatus(str, Enum):
    PENDING = "pending" #not used
    ACTIVE = "active"
    TERMINATED = "terminated"
    EXPIRED = "expired" #not used

