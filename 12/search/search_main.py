import logging
from flask import Blueprint, render_template, request

from search.function import search_posts_by_tag


logging.basicConfig(filename="log_search.log", level=logging.INFO)
logger_one = logging.getLogger("one")
console_handler = logging.StreamHandler()
formatter_one = logging.Formatter("%(asctime)s : %(message)s")
console_handler.setFormatter(formatter_one)
logger_one.addHandler(console_handler)
logger_one.warning("The logger 1 is working")


search_blueprint = Blueprint('search_blueprint', __name__)


@search_blueprint.route("/")
def page_index():
    """
     The view loads the main page of the search for posts by the occurrence of a substring
    """
    logging.info("The post search page has been requested.")
    return render_template('index.html')


@search_blueprint.route("/search")
def page_tag():
    """
    The view loads the page with the results of the search for posts by the occurrence of the substring
    """
    tag = request.args.get('s')
    list_post = search_posts_by_tag(tag)

    if list_post == []:
        logging.warning('An empty list of posts was received')
        return render_template('error_search.html')

    logging.info('The search results page has been loaded')
    return render_template('search.html', data=list_post, tag=tag)