import logging
from flask import Blueprint, render_template, request

from upload.function import add_post


logging.basicConfig(filename="log_search.log", level=logging.INFO)
logger_two = logging.getLogger("two")
console_handler = logging.StreamHandler()
formatter_two = logging.Formatter("%(asctime)s : %(message)s")
console_handler.setFormatter(formatter_two)
logger_two.addHandler(console_handler)
logger_two.warning("The logger 2 is working")


upload_blueprint = Blueprint('upload_blueprint', __name__)


@upload_blueprint.route("/post", methods=['POST', 'GET'])
def page_post_form():
    """
    The view loads a page with a form to upload a new post.
    """
    logging.info('The post download page was requested.')
    return render_template('post_form.html')


@upload_blueprint.route("/post/upload", methods=["POST"])
def page_post_upload():
    """
    The view loads a page with the results of loading a new post.
    """
    try:
        picture = request.files['picture']
        filename = picture.filename
        file_name = filename.split('.')

        if not file_name[-1] in ['jpeg', 'png', 'svg', 'gif']:
            logging.warning('An invalid file format has been uploaded')
            return render_template('error.html')

        description = request.form['content']

    except KeyError:
        logging.warning('File upload error')
        return render_template('error.html')

    else:
        path = f'static/images/{filename}'
        picture.save(path)
        dict_ = {'pic': path, 'content': description}

        add_post(dict_)
        logging.info('Post successfully added')
        return render_template('post_uploaded.html', dict_=dict_)
