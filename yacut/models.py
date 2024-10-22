from datetime import datetime as dt
from flask import url_for

from . import db


class URL_map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=dt.now())

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('redirect_short', short_id=self.short, _external=True),
        )

    def from_dict(self, data):
        setattr(self, 'original', data['url'])
        setattr(self, 'short', data['custom_id'])
