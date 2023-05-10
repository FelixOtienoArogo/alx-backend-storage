#!/usr/bin/env python3
"""Cache."""
import redis
import uuid
from typing import Union


class Cache:
    """Cache class."""

    def __init__(self):
        """Store an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store the input data in Redis."""
        key = uuid.uuid4()
        self._redis.set(f"{key}", data)
        return (f"{key}")
