from flask import Flask
from functions import get_all, get_by_pk, get_by_skill

app = Flask(__name__)

#   Creating a view to display all candidates on the root page.
@app.route('/')
def page_main():
    return get_all()

#   Creating a view to display the candidate's data on a separate page with a search by a given number.
@app.route('/candidates/<int:x>')
def page_candidates(x):
    return get_by_pk(x)

#   Creating a view to display the data of candidates with a given skill on a separate page
#   with a search for a given skill.
@app.route('/skills/<x>')
def page_skills(x):
    return get_by_skill(x)

if __name__ == '__main__':

    app.run()