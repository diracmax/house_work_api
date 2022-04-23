from dataclasses import dataclass


@dataclass
class InputUserDTO:
    user_id: int = None
    name: str = None
    raw_password: str = None
    line_token: str = None
