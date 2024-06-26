import redis


def create_redis():
    return redis.ConnectionPool(
        host='redis',
        port=6379,
        db=0,
        decode_responses=True
    )


pool = create_redis()


def get_redis():
    return redis.Redis(connection_pool=pool)

