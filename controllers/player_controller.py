from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player import Player
from models.player_history import Player_history
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository
import repositories.player_history_repository as player_history_repository

players_blueprint = Blueprint('players', __name__)

# GET list of players
@players_blueprint.route("/management/players", methods=['GET'] )
def players():
    list_of_players = player_repository.select_all_players() # NEW
    return render_template("management/players.html", all_players= list_of_players)

# SHOW
# GET '/players/<id>'
@players_blueprint.route('/management/player/<id>', methods=['GET'])
def show_player(id):
    player = player_repository.select(id)
    list_of_sessions = campaign_repository.select_all_campaigns() 
    if not player:
        return redirect("/management/players")
    return render_template ('/management/player.html', guest = player, all_sessions = list_of_sessions )

# CREATE new player
# POST '/management/players'
@players_blueprint.route("/management/players",  methods=['POST'])
def create_player():
    full_name = request.form['full_name']
    phone = request.form['phone']
    player = Player(full_name, phone)
    player_repository.save(player)
    return redirect('/management/players')

#EDIT player
# POST '/players/<id>/edit'
@players_blueprint.route("/management/players/<id>/edit", methods=['GET'])
def edit_player(id):
    player = player_repository.select(id)
    return render_template('/management/update_player_form.html', guest = player)


# UPDATE player
# POST (cannot be PUT) '/players/<id>'
@players_blueprint.route("/management/player/<id>/update", methods=['POST'])
def update_player(id):
    full_name = request.form['full_name']
    phone = request.form['phone']
    player = Player(full_name, phone,id)
    player_repository.update(player)
    return redirect(f'/management/player/{id}')
#urls are string already, and i want to pass a value for id, so i can do an f string.


# DELETE player
# DELETE '/players/<id>'
@players_blueprint.route("/management/player/<id>/delete", methods=['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/management/players')
    
#Add player to campaign
@players_blueprint.route("/management/player/<id>/join_session", methods=['POST'])
def add_player_to_session(id):
    campaign_id = request.form['campaign_id']
    campaign = campaign_repository.select(campaign_id)
    player = player_repository.select(id)
    player_history = Player_history(player, campaign)
    player_history_repository.save(player_history)
    return redirect('/management/players')