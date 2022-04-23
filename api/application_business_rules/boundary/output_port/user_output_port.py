from abc import ABC, abstractmethod

from fastapi.responses import JSONResponse
from fastapi import status

from enterprise_business_rules.dto.output_user_dto import OutputUserDTO


class UserOutputPort(ABC):
    @abstractmethod
    def create_view_for_save(self):
        pass
