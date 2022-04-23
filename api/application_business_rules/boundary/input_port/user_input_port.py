from abc import ABC, abstractmethod

from enterprise_business_rules.dto.input_user_dto import InputUserDTO


class UserInputPort(ABC):
    @abstractmethod
    def save(self, input_user_dto: InputUserDTO) -> str:
        pass
