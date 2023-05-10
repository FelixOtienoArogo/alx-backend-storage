#!/usr/bin/env python3
"""Cache."""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count calls of methods."""
    key = method.__qualname__

    @wraps(method)
    def incr(self, *args, **kwargs):
        """Wrap method."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return incr


class Cache:
    """Cache class."""

    def __init__(self):
        """Store an instance of the Redis client."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store the input data in Redis."""
        key = uuid.uuid4()
        self._redis.set(f"{key}", data)
        return (f"{key}")

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """Read from Redis."""
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """Get string."""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Get int."""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
