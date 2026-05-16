from pytest import mark
from src.connection.redis_connection import RedisConnectionHandle
from src.repository.redis_repository import RedisRepository

redis_conn = RedisConnectionHandle().set_conn()
Redis = RedisRepository(redis_conn)


class TestRedisClient:
    def test_set_a_new_key_and_get_it(self):
        # Given
        key = "test_key"
        value = "test_value"

        # When
        Redis.insert(key, value)

        # Then
        assert Redis.get(key) == value

    def test_update_a_key_and_get_it(self):
        # Given
        key = "test_key"
        value = "updated_value"

        previous_value = Redis.get(key)

        # When
        Redis.insert(key, value)

        # Then
        assert Redis.get(key) != previous_value

    def test_delete_a_key_and_get_it(self):
        # Given
        key = "test_key"

        # When
        Redis.delete(key)

        # Then
        assert Redis.get(key) is None

    def test_set_a_new_hash_and_get_it(self):
        # given
        key = "test_hash"
        value = {"field": "test_value", "field2": "test_value2"}

        # when
        Redis.insert_hash(key, value)

        # then
        assert Redis.get_hash(key, "field") == "test_value"
        assert Redis.get_hash(key, "field2") == "test_value2"

    def test_update_a_hash_and_get_it(self):
        # given
        key = "test_hash"
        field = "field"
        value = "updated_value"
        previous_value = Redis.get_hash(key, field)

        # when
        Redis.insert_hash(key, {field: value})

        # then
        assert Redis.get_hash(key, field) == value
        assert Redis.get_hash(key, field) != previous_value

    def test_delete_a_hash_and_get_it(self):
        # given
        key = "test_hash"
        field = "field"

        # when
        Redis.delete_hash(key, field)

        # then
        assert Redis.get_hash(key, field) is None
