import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/appointments', methods=('GET', 'PUT', 'DELETE'))
def appointments():
    if request.method == 'GET':
        return 'appointments'

@bp.route('/days', methods=(['GET']))
def days():
    if request.method == 'GET':
        db = get_db()
        try:
            days = db.execute(
                'SELECT * FROM days'
            ).fetchall()
        except db.IntegrityError:
            error = 'Error'
            print(error)
        return 'days'

@bp.route('/interviewers', methods=(['GET']))
def interviewers():
    if request.method == 'GET':
        db = get_db()
        try:
            interviewers = db.execute(
                'SELECT * FROM interviewers'
            ).fetchall()
            print(interviewers[0]['name'])
        except db.IntegrityError:
            error = 'Error'
            print(error)
        return 'interviewers'