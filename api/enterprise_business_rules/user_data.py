from dataclasses import dataclass


@dataclass
class UserData:
    user_id: int
    name: str
    hashed_password: str
    line_token: str
