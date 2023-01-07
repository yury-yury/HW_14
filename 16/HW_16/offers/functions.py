from HW_16.utils import Offer
from views import db


def get_offers():
    """

    """
    offers_list = []
    for item in Offer.query.all():
        offers_list.append({"id": item.id, "order_id": item.order_id, "executor_id": item.executor_id})

    return offers_list


def create_offer(offer):
    """

    """
    offer_new = Offer(id=offer.get("id"), order_id=offer.get("order_id"), executor_id=offer.get("executor_id"))
    db.session.add(offer_new)
    db.session.commit()

    res_dict = {"id": offer.id, "order_id": offer.order_id, "executor_id": offer.executor_id}

    return res_dict


def get_offer(offer):
    """

    """
    res_dict = {"id": offer.id, "order_id": offer.order_id, "executor_id": offer.executor_id}

    return res_dict


def update_offer(offer, offer_update):
    """

    """
    offer.id = offer_update.get("id")
    offer.order_id = offer_update.get("order_id")
    offer.executor_id = offer_update.get("executor_id")

    db.session.add(offer)
    db.session.commit()

    res_dict = {"id": offer.id, "order_id": offer.order_id, "executor_id": offer.executor_id}

    return res_dict