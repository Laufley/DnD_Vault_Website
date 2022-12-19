from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.campaign import Campaign
import repositories.campaign_repository as campaign_repository
import repositories.player_repository as player_repository

campaigns_blueprint = Blueprint("campaigns", __name__)


# GET list of sessions
@campaigns_blueprint.route("/management/sessions", methods=['GET'] )
def session():
    list_of_sessions = campaign_repository.select_all_campaigns() # NEW
    return render_template("management/sessions.html", all_sessions= list_of_sessions)

# SHOW
# GET '/campaigns/<id>'
@campaigns_blueprint.route('/management/session/<id>', methods=['GET'])
def show_session(id):
    session = campaign_repository.select(id)
    party = player_repository.players_per_campaign(id)
    if not session:
        return redirect('/management/sessions')
    return render_template ('/management/session.html', session = session, party = party)

# CREATE new campaign
# POST '/management/campaigns'
@campaigns_blueprint.route("/management/sessions",  methods=['POST'])
def create_campaign():
    title = request.form['title']
    genre = request.form['genre']
    dm = request.form['dm']
    max_capacity = request.form['max_capacity']
    price = request.form['price']
    details = request.form['details']
    session = Campaign(title, genre, dm, max_capacity, price, details)
    campaign_repository.save(session)
    return redirect('/management/sessions')

#EDIT campaign
# POST '/campaigns/<id>/edit'
@campaigns_blueprint.route("/management/sessions/<id>/edit", methods=['GET'])
def edit_campaign(id):
    session = campaign_repository.select(id)
    return render_template('/management/update_session_form.html', session = session)


# UPDATE session
# POST (cannot be PUT) '/sessions/<id>'
@campaigns_blueprint.route("/management/session/<id>/update", methods=['POST'])
def update_campaign(id):
    title = request.form['title']
    genre = request.form['genre']
    dm = request.form['dm']
    max_capacity = request.form['max_capacity']
    price = request.form['price']
    details = request.form['details']
    session = Campaign(title, genre, dm, max_capacity, price, details, id)
    campaign_repository.update(session)
    return redirect(f'/management/session/{id}')
#urls are string already, and i want to pass a value for id, so i can do an f string.


# DELETE session
# DELETE '/sessions/<id>'
@campaigns_blueprint.route("/management/session/<id>/delete", methods=['POST'])
def delete_session(id):
    campaign_repository.delete(id)
    return redirect('/management/sessions')
    


