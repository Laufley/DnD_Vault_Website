from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player import Player
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository

players_blueprint = Blueprint("players", __name__)

@players_blueprint.route('/management/players')
def management_players():
    return render_template('management/players.html', title="D&D Club")
