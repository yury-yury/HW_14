from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config['JSON_AS_ASCII'] = False
app.app_context().push()

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)


db.drop_all()
db.create_all()

user_john = User(id=1, name='John', age=30)
user_kate = User(id=2, name='Kate', age=31)

print(user_john, user_kate)

# db.session.add(user_john)
# db.session.add(user_kate)

users = [user_john, user_kate]

db.session.add_all(users)

print(db.session.new)   # List of undelivered changes

db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
