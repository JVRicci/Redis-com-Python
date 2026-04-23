from src.connection.redis_connection import RedisConnectionHandle
from src.repository.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().set_conn()

if __name__ == "__main__":
    redis_repository = RedisRepository(redis_conn)
    # redis_repository.insert("Estou", "funcionando")
    print(redis_repository.get("Estou"))

    redis_repository.insert_hash(
        "user:1", {"name": "John", "age": 30, "city": "New York"}
    )
    print(redis_repository.get_hash(key="user:1", value="name"))
