from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional


class URL_mapForm(FlaskForm):
    original_link = StringField(
        label='Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'), Length(1, 128)],
    )
    custom_id = StringField(
        label='Ваш вариант короткой ссылки', validators=[Length(1, 16), Optional()],
    )
    submit = SubmitField(label='Создать')