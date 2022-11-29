from flask import Flask

from functions import get_candidate, get_candidates_by_name, get_candidates_by_skill, get_all


app = Flask(__name__)

#   Creating a view to display all candidates on the root page.
@app.route('/')
def page_main():
    return get_all()

#   Creating a view to display the candidate's data on a separate page with a search by a given number.
@app.route('/candidate/<int:x>')
def page_candidate(x):
    return get_candidate(x)

#   Creating a view to display the list of candidates on a separate page with a search for a given part of the name.
@app.route('/search/<candidate_name>')
def page_candidates_by_name(candidate_name):
    return get_candidates_by_name(candidate_name)

#   Creating a view to display the data of candidates with a given skill on a separate page
#   with a search for a given skill.
@app.route('/skill/<skill_name>')
def page_candidates_by_skill(skill_name):
    return get_candidates_by_skill(skill_name)

app.run()