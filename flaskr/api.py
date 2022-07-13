import functools

import json

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/appointments', methods=('GET', 'PUT', 'DELETE'))
def appointments():
    if request.method == 'GET':
        db = get_db()
        try:
            appointments = db.execute(
                'SELECT * FROM appointments'
            ).fetchall()
            appointments_dict = {}
            for x in appointments:
                appointments_dict[x['id']] = {'time': x['time'], 'day_id': x['day_id']}
        except db.IntegrityError:
            error = 'Error'
            print(error)
        return json.dumps(appointments_dict)

@bp.route('/days', methods=(['GET']))
def days():
    if request.method == 'GET':
        db = get_db()
        try:
            days = db.execute(
                'SELECT * FROM days'
            ).fetchall()
            day_dict = {}
            for x in days:
                day_dict[x['id']] = {'name': x['name']}
        except db.IntegrityError:
            error = 'Error'
            print(error)
        return json.dumps(day_dict)

@bp.route('/interviewers', methods=(['GET']))
def interviewers():
    if request.method == 'GET':
        db = get_db()
        try:
            interviewers = db.execute(
                'SELECT * FROM interviewers'
            ).fetchall()
            print(interviewers[0].keys())
            interviewers_dict = {}
            for x in interviewers:
                interviewers_dict[x['id']] = {'name': x['name'], 'avatar': x['avatar']}
        except db.IntegrityError:
            error = 'Error'
            print(error)
        return json.dumps(interviewers_dict)