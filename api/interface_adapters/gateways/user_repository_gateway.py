from abc import abstractmethod, ABCMeta

from enterprise_business_rules.user_data import UserData


class UserRepositoryGateway(metaclass=ABCMeta):
    @abstractmethod
    def get(self, user_id: str) -> UserData:
        pass

    @abstractmethod
    def save(self, user_data: UserData) -> UserData:
        pass

    @abstractmethod
    def exist(self, user_id: str) -> bool:
        pass
