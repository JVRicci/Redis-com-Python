from redis import Redis


class RedisRepository:
    def __init__(self, redis_conn: Redis) -> None:
        self.__redis_conn = redis_conn

    def insert(self, key: str, value: any) -> None:
        self.__redis_conn.set(key, value)

    def get(self, key: str) -> any:
        value = self.__redis_conn.get(key)
        if value is not None:
            return value.decode("utf-8")
        return None

    def insert_hash(self, key: str, value: dict) -> None:
        self.__redis_conn.hset(key, mapping=value)

    def get_hash(self, key: str, value: str) -> any:
        value = self.__redis_conn.hget(key, value)
        if value is not None:
            return value.decode("utf-8")
        return None

    def insert_ex(self, key: str, value: any, ex: int) -> None:
        self.__redis_conn.set(key, value, ex=ex)

    def insert_hash_ex(self, key: str, field: str, value: any, ex: int) -> None:
        self.__redis_conn.hset(key, field, value)
        self.__redis_conn.expire(key, ex)

    def delete(self, key: str) -> None:
        self.__redis_conn.delete(key)

    def delete_hash(self, key: str, field: str) -> None:
        self.__redis_conn.hdel(key, field)

    def return_all_keys(self) -> list:
        return self.__redis_conn.keys()
