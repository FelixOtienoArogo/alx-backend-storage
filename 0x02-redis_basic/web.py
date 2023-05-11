#!/usr/bin/env python3
"""Module for Implementing an expiring web cache and tracker."""

from functools import wraps
import redis
import requests
from typing import Callable

_redis = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """Decortator to count how many request has been made."""
    @wraps(method)
    def wrapper(url):
        """Wrap the method."""
        key = f"count:{url}"
        _redis.incr(key)
        count = _redis.get(key)
        if count is not None:
            return count.decode('utf-8')
        else:
            page = method(url)
            _redis.setex(key, 10, page)
            return page

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """Get the html content of a web page."""
    req = requests.get(url)
    return req.text
