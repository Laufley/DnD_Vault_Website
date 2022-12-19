from flask import Flask, render_template, request, redirect, Blueprint

from models.player import Player
from models.campaign import Campaign
from models.player_history import Player_history
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository
import repositories.player_history_repository as player_history_repository

public_blueprint = Blueprint("public", __name__)

@public_blueprint.route('/about')
def about():
    return render_template('public/about.html', title="D&D Club")

@public_blueprint.route('/contact')
def contact():
    return render_template('public/contact.html', title="D&D Club")

@public_blueprint.route('/dm')
def dm():
    return render_template('public/dm.html', title="D&D Club")

@public_blueprint.route('/guides')
def guides():
    return render_template('public/guides.html', title="D&D Club")

@public_blueprint.route('/tips')
def tips():
    return render_template('public/tips.html', title="D&D Club")

@public_blueprint.route('/upcoming')
def upcoming():
    return render_template('public/upcoming.html', title="D&D Club")

@public_blueprint.route('/management/login')
def management_login():
    return render_template('management/login.html', title="D&D Club")

@public_blueprint.route('/management/board')
def management_board():
    return render_template('management/board.html', title="D&D Club")


# # GET list of campaigns
@public_blueprint.route("/home", methods=['GET'] )
def campaigns():
    list_of_campaigns = campaign_repository.select_all_campaigns() # NEW
    return render_template('/public/home.html', all_campaigns= list_of_campaigns)

# SHOW
# GET '/campaigns/<id>'
@public_blueprint.route('/campaign/<id>', methods=['GET'])
def show_campaign(id):
    campaign = campaign_repository.select(id)
    if not campaign:
        return redirect('/campaigns')
    return render_template ('public/campaigns/campaign.html', campaign = campaign)




        