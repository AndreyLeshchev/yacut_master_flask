from datetime import datetime as dt
import random
import string

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=True)
    timestamp = db.Column(db.DateTime, index=True, default=dt.now())

    @staticmethod
    def get_unique_short_id():
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6,
            )
        )