import random
import string


def genarate_short_link():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6,
        )
    )