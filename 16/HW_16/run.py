from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from users.views import users_blueprint
from orders.views import orders_blueprint
from offers.views import offers_blueprint

from utils import create_start_data_base


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config['JSON_AS_ASCII'] = False
app.app_context().push()
db = SQLAlchemy(app)

create_start_data_base()

app.register_blueprint(users_blueprint, url_prefix='/users')
app.register_blueprint(orders_blueprint, url_prefix='/orders')
app.register_blueprint(offers_blueprint, url_prefix='/offers')

if __name__ == '__main__':

    app.run(debug=True)