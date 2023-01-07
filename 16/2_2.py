from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.app_context().push()
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    passport_number = db.Column(db.String(3), unique=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, db.CheckConstraint("age > 18"))
    group_id = db.Column(db.Integer, db.ForeignKey("group.id"))

    group = relationship("Group")


class Group(db.Model):
    __tablename__ = "group"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    users = relationship("User")


db.create_all()

# PK Unique exception
try:
    user_01 = User(id=1, name="John", age=30, passport_number='123')

    with db.session.begin():
        db.session.add(user_01)

    user_01_copy = User(id=1, name="John", age=30, passport_number='456')

    with db.session.begin():
        db.session.add(user_01_copy)

except Exception as e:
    print(e)

# Column Unique exception
try:
    user_02 = User(id=2, name="Kate", age=31, passport_number='123')

    with db.session.begin():
        db.session.add(user_02)

except Exception as e:
    print(e)

# Check exception
try:
    user_03 = User(id=3, name="Artur", age=15, passport_number='000')

    with db.session.begin():
        db.session.add(user_03)

except Exception as e:
    print(e)

# Nullable exception
try:
    user_04 = User(id=4, name=None, age=25, passport_number='888')

    with db.session.begin():
        db.session.add(user_04)

except Exception as e:
    print(e)

if __name__ == "__main__":
    app.run(debug=True)

