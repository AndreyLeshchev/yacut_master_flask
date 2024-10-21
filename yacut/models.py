from datetime import datetime as dt
import random
import string
from flask import url_for

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=dt.now())

    @staticmethod
    def get_unique_short_id():
        return ''.join(
            random.choices(
                string.ascii_letters + string.digits,
                k=6,
            )
        )

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_short', slug=self.short, _external=True),
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
