import json
from flask import Blueprint, request, Flask
from flask_sqlalchemy import SQLAlchemy

from HW_16.utils import User
from functions import get_all_users, create_user, get_user, update_user


users_blueprint = Blueprint('users_blueprint', __name__, url_prefix='/users')

@users_blueprint.route('/', methods=['GET', 'POST'])
def get_or_create_users():
    """

    """
    if request.method == 'GET':
        return json.dumps(get_all_users())

    elif request.method == 'POST':
        user = request.json
        return json.dumps(create_user(user))


@users_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_user(id):
    """

    """
    user = User.query.get(id)

    if request.method == 'GET':
        return json.dumps(get_user(user))

    elif request.method == 'PUT':
        user_update = request.json

        return json.dumps(update_user(user, user_update))

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()

        return json.dumps({"message": "The database object was successfully deleted"})

