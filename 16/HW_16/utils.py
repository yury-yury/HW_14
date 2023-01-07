import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from run import db


class User(db.Model):
    """
    The class inherits from db.Model and is designed to represent the "users" table when working
    in a database using the Flask-Sqlalchemy framework. Contains a description of the column properties
    and the installed database dependencies.
    """
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age >= 18"))
    email = db.Column(db.String, unique=True)
    phone = db.Column(db.String(12), unique=True)
    role = db.Column(db.String)

    customers = db.relationship('Customer', cascade='save-update, merge, delete')
    executors = db.relationship('Executor', cascade='save-update, merge, delete')


class Customer(db.Model):
    """
    The class inherits from db.Model is auxiliary and is designed to separate users depending on their role
    and represents the "customers" table when working in a database using the Flask-Sqlalchemy framework.
    Contains a description of the column properties and the installed database dependencies.
    """
    __tablename__ = "customers"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)

    orders = db.relationship('Order', cascade='save-update, merge, delete')


class Executor(db.Model):
    """
    The class inherits from db.Model is auxiliary and is designed to separate users depending on their role
    and represents the "executors" table when working in a database using the Flask-Sqlalchemy framework.
    Contains a description of the column properties and the installed database dependencies.
    """
    __tablename__ = "executors"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), primary_key=True)

    orders = db.relationship('Order', cascade='save-update, merge, delete')
    offers = db.relationship('Offer', cascade='save-update, merge, delete')


class Order(db.Model):
    """
    The class inherits from db.Model and is designed to represent the "orders" table when working
    in a database using the Flask-Sqlalchemy framework. Contains a description of the column properties
    and the installed database dependencies.
    """
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    start_date = db.Column(db.String())
    end_date = db.Column(db.String())
    address = db.Column(db.String)
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.user_id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executors.user_id"))

    offers = db.relationship('Offer', cascade='save-update, merge, delete')


class Offer(db.Model):
    """
    The class inherits from db.Model and is designed to represent the "offers" table when working
    in a database using the Flask-Sqlalchemy framework. Contains a description of the column properties
    and the installed database dependencies.
    """
    __tablename__ = "offers"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executors.user_id"))


def load_data(file):
    """
    The function takes as an argument the name of the JSON file that contains the source data for the database,
    in the form of a string, reads the information from the opened file and returns the data in the form
    of a list of dictionaries.
    """
    with open(f'{file}', 'r', encoding='utf-8') as file:

        file_list = json.load(file)

    return file_list


def create_start_data_base():
    """

    """
    db.drop_all()
    db.create_all()

    # Preparation of initial data for database creation.
    users = []
    for item in load_data('data/users.json'):
        users.append(User(id=item['id'], first_name=item['first_name'], last_name=item['last_name'], age=item['age'],
                          email=item['email'], role=item['role'], phone=item['phone']))

    db.session.begin()
    db.session.add_all(users)

    customers = []
    for item in User.query.filter(User.role == 'customer').all():
        customers.append(Customer(user_id=item.id))

    db.session.add_all(customers)

    executors = []
    for item in User.query.filter(User.role == 'executor').all():
        executors.append(Executor(user_id=item.id))

    db.session.add_all(executors)

    orders = []
    for item in load_data('data/orders.json'):
        orders.append(Order(id=item['id'], name=item['name'], description=item['description'],
                            start_date=item['start_date'], end_date=item['end_date'], address=item['address'],
                            price=item['price'], customer_id=item['customer_id'], executor_id=item['executor_id']))

    db.session.add_all(orders)

    offers = []
    for item in load_data('data/offers.json'):
        offers.append(Offer(id=item['id'], order_id=item['order_id'], executor_id=item['executor_id']))

    db.session.add_all(offers)
    db.session.commit()
