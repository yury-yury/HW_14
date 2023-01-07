from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import or_, desc, func


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

# Data preparation
group_01 = Group(id=1, name="Group #1")
group_02 = Group(id=2, name="Group #2")

user_01 = User(id=1, name="John", age=20, group=group_01)
user_02 = User(id=2, name="Kate", age=22, group=group_02)
user_03 = User(id=3, name="Artur", age=23, group=group_01)
user_04 = User(id=4, name="Maxim", age=24, group=group_01)
user_05 = User(id=5, name="Lily", age=25, group=group_02)
user_06 = User(id=6, name="Mary", age=26, group=group_02)

with db.session.begin():
    db.session.add_all([user_01, user_02, user_03, user_04, user_05, user_06])

# Requests to delete data by id
user = User.query.get(2)

db.session.delete(user)
db.session.commit()

user = User.query.get(2)
print(user is None)

# Requests to delete data by condition
db.session.query(User).filter(User.name == 'Maxim').delete()
db.session.commit()

user = User.query.filter(User.name == 'Maxim').all()
print(f'User: {user}')

if __name__ == '__main__':
    app.run(debug=True)