import datetime
from enterprise_business_rules.dto.output_user_dto import OutputUserDTO
from werkzeug.exceptions import NotFound

from application_business_rules.boundary.output_port.user_output_port import UserOutputPort
from enterprise_business_rules.dto.input_user_dto import InputUserDTO
from enterprise_business_rules.entity.user import User
from interface_adapters.gateways.user_repository_gateway import UserRepositoryGateway
from application_business_rules.boundary.input_port.user_input_port import UserInputPort


class UserHandleInteractor(UserInputPort):
    def __init__(self, presenter: UserOutputPort, repository: UserRepositoryGateway):
        self.presenter = presenter
        self.repository = repository

    def save(self, input_user_dto: InputUserDTO):
        user = User(name=input_user_dto.name, hashed_password=input_user_dto.raw_password,
                    line_token=input_user_dto.line_token)
        self.repository.save(user)
        return self.presenter.create_view_for_save()
