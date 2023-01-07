import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.app_context().push()

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


db.drop_all()
db.create_all()

user_john = User(name='John', age=30)
user_kate = User(name='Kate', age=31)

print(user_john.id, user_kate.id)

# db.session.add(user_john)
# db.session.add(user_kate)

users = [user_john, user_kate]
db.session.add_all(users)

print(db.session.new)   # List of undelivered changes

db.session.commit()

@app.route("/users/first")
def get_first_user():
    user = User.query.first()
    return json.dumps({"id": user.id,
                        "name": user.name,
                        "age": user.age})


@app.route("/users/count")
def get_users_count():
    user_count = User.query.count()
    return json.dumps(user_count)


@app.route("/users")
def get_users():
    user_list = User.query.all()
    user_response = []

    for user in user_list:
        user_response.append(
            {"id": user.id,
            "name": user.name,
            "age": user.age})

    return json.dumps(user_response)


@app.route("/users/<int:sid>")
def get_user(sid):
    user = User.query.get(sid)
    return json.dumps({
            "id": user.id,
            "name": user.name,
            "age": user.age})


if __name__ == '__main__':
    app.run(debug=True)