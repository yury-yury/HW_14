import json
from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

from ..run import app, db
from HW_16.utils import Order
from functions import get_orders, create_order, get_order, update_order


orders_blueprint = Blueprint('orders_blueprint', __name__, url_prefix='/orders' )


@orders_blueprint.route('/', methods=['GET', 'POST'])
def get_or_create_orders():
    """

    """
    if request.method == 'GET':
        return json.dumps(get_orders())

    elif request.method == 'POST':
        order = request.json
        return json.dumps(create_order(order))


@orders_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_or_update_or_delete_order(id):
    """

    """
    order = Order.query.get(id)

    if request.method == 'GET':
        return json.dumps(get_order(order))

    elif request.method == 'PUT':
        order_update = request.json
        return json.dumps(update_order(order, order_update))

    elif request.method == 'DELETE':
        db.session.delete(order)
        db.session.commit()
        return json.dumps({"message": "The database object was successfully deleted"})
