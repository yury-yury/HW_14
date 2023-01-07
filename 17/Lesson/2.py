from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

# Making a scheme
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    age = fields.Int()


# Making a conversion to a dictionary
user = User(id=1, name="jane", age=19)
user_schema = UserSchema()
result = user_schema.dump(user)

print(type(result))                                 # <class 'dict'>
print(result["name"], result["age"])                # jane 19

# Making a conversion to a string
user = User(id=1, name="jane", age=19)
user_schema = UserSchema()
result = user_schema.dumps(user)

print(type(result))                                 # <class 'str'>
print(result)                                       # {"age": 19, "id": 1, "name": "jane"}


# We are converting a group of objects into a string and a Python object
u1 = User(id=2, name="John", age=30)
u2 = User(id=3, name="Kate", age=30)
u3 = User(id=4, name="Mary", age=30)
u4 = User(id=5, name="Max", age=30)

user_schema = UserSchema(many=True)

print(type(user_schema.dump([u1, u2, u3, u4])))     # <class 'list'>
print(user_schema.dump([u1, u2, u3, u4]))           # [{'id': 2, 'name': 'John', 'age': 30},
                                                    # {'id': 3, 'name': 'Kate', 'age': 30},
                                                    # {'id': 4, 'name': 'Mary', 'age': 30},
                                                    # {'id': 5, 'name': 'Max', 'age': 30}]

print(type(user_schema.dumps([u1, u2, u3, u4])))    # <class 'str'>
print(user_schema.dumps([u1, u2, u3, u4]))          # [{"id": 2, "name": "John", "age": 30},
                                                    # {"id": 3, "name": "Kate", "age": 30},
                                                    # {"id": 4, "name": "Mary", "age": 30},
                                                    # {"id": 5, "name": "Max", "age": 30}]

# Doing deserialization into a database object
user_json_str = '{"age": 30, "name": "John"}'
user_schema = UserSchema()

user_dict = user_schema.loads(user_json_str)
user = User(**user_dict)

print(type(user))                                   # <class '__main__.User'>
print(user.name, user.age)                          # John 30

if __name__ == '__main__':
    app.run(debug=False)