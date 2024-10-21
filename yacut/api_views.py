from http import HTTPStatus
from flask import jsonify, request
from re import match

from . import app, db
from .models import URL_map
from .error_handlers import CustomApiException


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if not url_map:
        raise CustomApiException('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise CustomApiException('Отсутствует тело запроса')
    if 'url' not in data:
        raise CustomApiException('"url" является обязательным полем!')
    if 'custom_id' not in data:
        data['custom_id'] = URL_map.get_unique_short_id()
    if not match(r'^[a-zA-Z0-9]{1,16}$', data['custom_id']):
        raise CustomApiException('Указано недопустимое имя для короткой ссылки')
    if URL_map.query.filter_by(short=data['custom_id']).first():
        raise CustomApiException(f'Имя "{data["custom_id"]}" уже занято.')
    url_map = URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), HTTPStatus.CREATED
