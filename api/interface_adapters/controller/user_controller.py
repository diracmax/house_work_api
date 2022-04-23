from application_business_rules.user_handle_interactor import UserHandleInteractor
from application_business_rules.boundary.output_port.user_output_port import UserOutputPort
from application_business_rules.user_handle_interactor import UserHandleInteractor
from enterprise_business_rules.dto.input_user_dto import InputUserDTO
from interface_adapters.gateways.user_repository_gateway import UserRepositoryGateway
from starlette.requests import Request


class UserController:
    def __init__(self, presenter: UserOutputPort, repository: UserRepositoryGateway):
        self.presenter = presenter
        self.repository = repository

    def save(self, request: Request):
        name: str = request.json["name"]
        raw_password: str = request.password
        line_token: str = request.line_token
        input_user_dto: InputUserDTO = InputUserDTO(
            name=name, raw_password=raw_password, line_token=line_token)

        return UserHandleInteractor(self.presenter, self.repository).save(input_user_dto)
