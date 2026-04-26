from datetime import datetime
from src.connection.redis_connection import RedisConnectionHandle
from src.repository.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().set_conn()

if __name__ == "__main__":
    redis_repository = RedisRepository(redis_conn)

    options = {
        1: "Insert",
        2: "Get",
        3: "Insert Hash",
        4: "Get Hash",
        5: "Insert with Expiration",
        6: "Insert Hash with Expiration",
    }

    select = int(
        input(
            "Select an option: \n1 - Insert\n2 - Get\n3 - Insert Hash\n4 - Get Hash\n5 - Insert with Expiration\n6 - Insert Hash with Expiration\n"
        )
    )

    if select in [1, 3, 5, 6]:
        key = input("Enter the key: ")
        value = input("Enter the value: ")

        if select == 1:
            redis_repository.insert(key, value)
        elif select == 3:
            field = input("Enter the field: ")
            redis_repository.insert_hash(key, {field: value})
        elif select == 5:
            ex = int(input("Enter the expiration time in seconds: "))
            redis_repository.insert_ex(key, value, ex)
        elif select == 6:
            field = input("Enter the field: ")
            ex = int(input("Enter the expiration time in seconds: "))
            redis_repository.insert_hash_ex(key, field, value, ex)

    elif select in [2, 4]:
        key = input("Enter the key: ")

        if select == 2:
            print(
                redis_repository.get(key)
                if redis_repository.get(key)
                else "Key not found"
            )
        elif select == 4:
            field = input("Enter the field: ")
            print(
                redis_repository.get_hash(key, field)
                if redis_repository.get_hash(key, field)
                else "Field not found"
            )
