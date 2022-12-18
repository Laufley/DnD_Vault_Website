from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player import Player
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository

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
    if not player:
        return redirect("/management/players")
    return render_template ('/management/player.html', guest = player)

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
    

