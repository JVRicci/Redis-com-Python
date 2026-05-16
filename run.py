from datetime import datetime
from src.connection.redis_connection import RedisConnectionHandle
from src.repository.redis_repository import RedisRepository
from src.repository.strategy import (
    RegisterValueMap,
    GetValueMap,
    InsertHashMap,
    GetHashMap,
    InsertWithExpiration,
    InsertHashWithExpiration,
    DeleteKey,
    DeleteHash,
    ReturnAllKeys,
)

redis_conn = RedisConnectionHandle().set_conn()

if __name__ == "__main__":
    redis_repository = RedisRepository(redis_conn)

    strategies = {
        1: RegisterValueMap(),
        2: GetValueMap(),
        3: InsertHashMap(),
        4: GetHashMap(),
        5: InsertWithExpiration(),
        6: InsertHashWithExpiration(),
        7: DeleteKey(),
        8: DeleteHash(),
        9: ReturnAllKeys(),
    }

    menu = """Escolha uma opção:
1 - Registrar valor em um mapa
2 - Obter valor de um mapa
3 - Registrar valor em um hash
4 - Obter valor de um hash
5 - Registrar valor com expiração
6 - Registrar valor em hash com expiração
7 - Deletar chave
8 - Deletar hash
9 - Retornar todas as chaves

Opção: """

    select = int(input(menu))

    strategy = strategies.get(select)

    if not strategy:
        print("Opção inválida.")
    else:
        result = strategy.execute(redis_repository)
        print(result)
