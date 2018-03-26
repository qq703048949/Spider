import hashlib
import os
from functools import wraps
import codecs
import time

def cache(cachetime):
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            result = None
            son_obj = args[0]
            url = args[1]
            if son_obj.cache:
                try:


                    son_obj.logger.info(url+' read cache')
                    result = son_obj.cache[url]

                except KeyError as e:
                    print(e)

            if result is None:
                son_obj.throttle.wait(url)
                son_obj.logger.info('get content from internet')
                result = son_obj.get_content.__wrapped__(son_obj, url)
                if son_obj.cache:
                    son_obj.cache[url] = result

            return result['html']

        return wrapper
    return decorator



