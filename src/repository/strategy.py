from abc import abstractmethod


class Strategy:
    @abstractmethod
    def execute(self, redis_repository):
        pass


class RegisterValueMap(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        value = input("Insira um valor:")
        redis_repository.insert(key, value)
        return f"O valor {value} foi inserido com a key {key}."


class GetValueMap(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        value = redis_repository.get(key)
        if value is None:
            return f"O valor da key {key} é: {value}"
        return "Nenhum valor encontrado"


class InsertHashMap(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        field = input("Insira um field:")
        value = input("Insira um valor:")
        redis_repository.insert_hash(key, field, value)
        return f"O field {field} da key {key} foi inserido com o valor {value}."


class GetHashMap(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        field = input("Insira um field:")
        value = redis_repository.get_hash(key, field)
        if value is None:
            return f"O field {field} da key {key} não existe."
        return f"O valor do field {field} da key {key} é: {value}"


class InsertWithExpiration(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        value = input("Insira um valor:")
        expiration = int(input("Insira o tempo de expiração (em segundos):"))

        redis_repository.insert_with_expiration(key, value, expiration)
        return f"O valor {value} foi inserido com a key {key} e expiração de {expiration} segundos."


class InsertHashWithExpiration(Strategy):
    def execute(self, redis_repository):
        key = input("Insira uma key:")
        field = input("Insira um field:")
        value = input("Insira um valor:")
        expiration = int(input("Insira o tempo de expiração (em segundos):"))

        redis_repository.insert_hash_with_expiration(key, field, value, expiration)
        return f"O field {field} da key {key} foi inserido com o valor {value} e expiração de {expiration} segundos."
