from db.run_sql import run_sql

from models.player_history import Player_history
from models.campaign import Campaign
from models.player import Player
import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository

def save(player_history):
    sql = "INSERT INTO players_history ( player_id, campaign_id ) VALUES ( %s, %s) RETURNING id"
    values = [player_history.player.id, player_history.campaign.id]
    results = run_sql(sql, values)
    player_history.id = results[0]['id']
    return player_history

def select_all():
    all_players_history = []

    sql = "SELECT * FROM players_history"
    results = run_sql(sql)

    for row in results:
        player = player_repository.select(row['player_id'])
        campaign = campaign_repository.select(row['campaign_id'])
        player_history = Player_history(player, campaign, row['id'])
        all_players_history.append(player_history)
    return all_players_history


def delete_all():
    sql = "DELETE FROM players_history"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players_history WHERE id = %s"
    values = [id]
    run_sql(sql, values)