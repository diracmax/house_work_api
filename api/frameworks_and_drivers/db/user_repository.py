from enterprise_business_rules.entity.user import User
from enterprise_business_rules.user_data import UserData
from interface_adapters.gateways.user_repository_gateway import UserRepositoryGateway
from werkzeug.exceptions import Conflict, NotFound


class UserRepository(UserRepositoryGateway):

    def __init__(self, connection):
        self.conn = connection

    def exist(self, user_id: int) -> bool:
        cursor = self.conn.cursor()

        # memo_idがあるかどうか確認する
        query = "SELECT EXISTS(SELECT * FROM USERS WHERE user_id = %s)"
        cursor.execute(query, [user_id])
        result: tuple = cursor.fetchone()

        # DBクライアントをcloseする
        cursor.close()

        # 検索結果が1件あるかどうかで存在を確認する
        if result[0] == 1:
            return True
        else:
            return False

    def get(self, user_id: int) -> User:

        # 指定されたidがあるかどうか確認する
        is_exist: bool = self.exist(user_id)

        if not is_exist:
            raise NotFound(f'user_id [{user_id}] is not registered yet.')

        # DBクライアントを作成する
        cursor = self.conn.cursor()

        # memo_idで検索を実行する
        query = "SELECT * FROM USERS WHERE user_id = %s"
        cursor.execute(query, [user_id])
        result: tuple = cursor.fetchone()

        # DBクライアントをcloseする
        cursor.close()

        return User(user_id=user_id, name=result[1], hashed_password=result[2], line_token=result[3])

    def save(self, user: User) -> bool:
        user_id: int = user.user_id
        name: str = user.name
        hashed_password: str = user.hashed_password
        line_token: str = user.line_token

        # 指定されたidがあるかどうか確認する
        is_exist = self.exist(user_id)

        if is_exist:
            raise Conflict(f'user_id [{user_id}] is already registered.')

        # DBクライアントを作成する
        cursor = self.conn.cursor()

        # memoを保存する
        query = "INSERT INTO USERS (user_id, name, hashed_password, line_token) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (user_id, name, hashed_password, line_token))

        # DBクライアントをcloseする
        cursor.close()

        return True
