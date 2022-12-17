from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.campaign import Campaign
import repositories.campaign_repository as campaign_repository
import repositories.player_repository as player_repository

campaigns_blueprint = Blueprint("campaigns", __name__)



@campaigns_blueprint.route('/campaigns')
def campaigns():
    return render_template('campaigns/campaigns.html', title="D&D Club")

@campaigns_blueprint.route('/management/sessions')
def management_sessions():
    return render_template('management/sessions.html', title="D&D Club")
