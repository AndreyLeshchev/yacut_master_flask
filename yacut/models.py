from datetime import datetime as dt

from . import db
from .utils import genarate_short_link


class UrlMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(128), nullable=False)
    short = db.Column(db.String(16), unique=True, default=genarate_short_link())
    timestamp = db.Column(db.DateTime, index=True, default=dt.now())