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

# Data requests

# SQL -> WHERE
# query = User.query.filter(User.name == 'Maxim')
query = db.session.query(User).filter(User.name == 'Maxim')
print(f'Request {query}')
print(f'Result: {query.first().name}')

# SQL -> WHERE (Requered record)
# query = User.query.filter(User.name == 'Maxim')
query = db.session.query(User).filter(User.name == 'Maxim')
print(f'Request {query}')
print(f'Result: {query.one()}')

# SQL -> WHERE ... AND ...
# query = User.query.filter(User.id <= 5, User.age > 20)
query = db.session.query(User).filter(User.id <= 5, User.age > 20)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... LIKE ...
# query = User.query.filter(User.name.like("L%"))
query = db.session.query(User).filter(User.name.like("L%"))
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... OR ...
# query = User.query.filter(or_(User.id <= 5, User.age > 20))
query = db.session.query(User).filter(or_(User.id <= 5, User.age > 20))
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... IS NULL
# query = User.query.filter(User.passport_number == None)
query = db.session.query(User).filter(User.passport_number == None)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... IS NOT NULL
# query = User.query.filter(User.passport_number != None)
query = db.session.query(User).filter(User.passport_number != None)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... IN ( ... )
# query = User.query.filter(User.id.in_([1, 2]))
query = db.session.query(User).filter(User.id.in_([1, 2]))
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> WHERE ... BETWEEN ...
# query = User.query.filter(User.id.between(1, 6))
query = db.session.query(User).filter(User.id.between(1, 6))
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> LIMIT
# query = User.query.limit(2)
query = db.session.query(User).limit(2)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> LIMIT ... OFFSET ...
# query = User.query.limit(2).offset(2)
query = db.session.query(User).limit(2).offset(2)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> ORDER BY
# query = User.query.order_by(User.id)
query = db.session.query(User).order_by(User.id)
print(f'Request {query}')
print(f'Result: {query.all()}')

query = db.session.query(User).order_by(desc(User.id))
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> INNER JOIN
#
query = db.session.query(User.name, Group.name).join(Group)
print(f'Request {query}')
print(f'Result: {query.all()}')

# SQL -> GROUP BY ( ... )
#
column = func.count(User.id)
query = db.session.query(column).join(Group).filter(Group.id == 1).group_by(Group.id)
print(f'Request {query}')
print(f'Result: {query.scalar()}')

if __name__ == '__main__':
    app.run(debug=True)
    