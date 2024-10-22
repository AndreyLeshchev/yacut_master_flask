import random
import string

from .models import URL_map


def get_unique_short_id():
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    if not URL_map.query.filter_by(short=short).first():
        return short
    return get_unique_short_id()