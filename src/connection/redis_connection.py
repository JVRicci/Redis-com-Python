from redis import Redis
from src.connection.connection_options import connection_options


class RedisConnectionHandle:
    def __init__(self) -> None:
        self.__host = connection_options["HOST"]
        self.__port = connection_options["PORT"]
        self.__db = connection_options["DB"]
        self.__connection = None

    def set_conn(self) -> Redis:
        self.__connection = Redis(host=self.__host, port=self.__port, db=self.__db)
        return self.__connection

    def get_conn(self) -> Redis:
        if not self.__connection:
            self.set_conn()
        return self.__connection
