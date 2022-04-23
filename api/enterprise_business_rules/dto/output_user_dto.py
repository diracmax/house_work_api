from dataclasses import dataclass


@dataclass
class OutputUserDTO:
    user_id: int
    name: str
