from flask import flash, render_template, abort, url_for, redirect

from . import app, db
from .forms import URL_mapForm
from .models import URL_map


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        if not form.custom_id.data:
            short = URL_map.get_unique_short_id()
        if URL_map.query.filter_by(short=short).first():
            flash(f'Ссылка {short} уже занята.', 'negative_response')
            return render_template('index.html', form=form)
        url_map = URL_map(
            original=form.original_link.data,
            short=short,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(
            url_for(
                'redirect_short', slug=short, _ext_external=True,
            ), 'positive_response',
        )
    return render_template('index.html', form=form)


@app.route('/<string:slug>', methods=['GET'])
def redirect_short(slug):
    url_map = URL_map.query.filter_by(short=slug).first()
    if not url_map:
        abort(404)
    return redirect(url_map.original)