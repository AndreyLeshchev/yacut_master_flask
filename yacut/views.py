from flask import flash, render_template, abort, url_for, redirect

from . import app, db
from .forms import URL_mapForm
from .models import URL_map
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        if URL_map.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!', 'not_unique')
            return render_template('index.html', form=form)
        url_map = URL_map(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(
            url_for(
                'redirect_short', short_id=short, _external=True,
            ), 'ok_unique',
        )
    return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_short(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if not url_map:
        abort(404)
    return redirect(url_map.original)