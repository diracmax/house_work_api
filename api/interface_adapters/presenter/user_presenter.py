from fastapi.responses import JSONResponse
from fastapi import status
from application_business_rules.boundary.output_port.user_output_port import UserOutputPort
from enterprise_business_rules.user_data import UserData


class UserPresenter(UserOutputPort):
    def create_view_for_save(self):
        return JSONResponse(content={"message": "success"}, status_code=status.HTTP_201_CREATED)
