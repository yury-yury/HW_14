from flask import Flask, request, render_template

from search.search_main import search_blueprint
from upload.upload_main import upload_blueprint

app = Flask(__name__)


app.register_blueprint(search_blueprint)

app.register_blueprint(upload_blueprint)


if __name__ == '__main__':
    app.run(debug=False)