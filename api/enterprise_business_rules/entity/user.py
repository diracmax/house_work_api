class User(object):

    def __init__(self, user_id, name, hashed_password, line_token):
        assert isinstance(user_id, int)
        assert isinstance(name, str)
        assert isinstance(hashed_password, str)
        assert isinstance(line_token, str)
        self.__user_id = user_id
        self.__name = name
        self.__hashed_password = hashed_password
        self.__line_token = line_token

    @property
    def user_id(self):
        return self.__user_id

    @property
    def name(self):
        return self.__name

    @property
    def hashed_password(self):
        return self.__hashed_password

    @property
    def line_token(self):
        return self.__line_token
