from flask import render_template

from app import app
from status_build import build_status


@app.route('/')
@app.route('/index')
def index():
    title = "Status"
    display_status = build_status()

    return render_template('status.html', title='Status', display_status=display_status)
