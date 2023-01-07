import json
from flask import Blueprint, request
from flask_sqlalchemy import SQLAlchemy

from HW_16.utils import Offer
from functions import get_offers, create_offer, get_offer, update_offer


offers_blueprint = Blueprint('offers_blueprint', __name__, url_prefix='/offers')


@offers_blueprint.route('/', methods=['GET', 'POST'])
def get_or_create_offers():
    """

    """
    if request.method == 'GET':
        return json.dumps(get_offers())

    elif request.method == 'POST':
        offer = request.json
        return json.dumps(create_offer(offer))


@offers_blueprint.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_offer(id):
    """

    """
    offer = Offer.query.get(id)

    if request.method == 'GET':
        return json.dumps(get_offer(offer))

    elif request.method == 'PUT':
        offer_update = request.json
        return json.dumps(update_offer(offer, offer_update))


    elif request.method == 'DELETE':

        db.session.delete(offer)
        db.session.commit()

        return json.dumps({"message": "The database object was successfully deleted"})
