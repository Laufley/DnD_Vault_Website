from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.player_history import Player_history
import repositories.player_history_repository as player_history_repository
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository

players_history_blueprint = Blueprint("players_history", __name__)



