from db.run_sql import run_sql

from models.player import Player
from models.campaign import Campaign

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)
    
def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(player):
    sql = "INSERT INTO players (full_name, phone) VALUES ( %s, %s ) RETURNING *"
    values = [player.full_name, player.phone]
    results = run_sql( sql, values )
    player.id = results[0]['id']
    return player


def select_all_players():
    list_of_players = []
    
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['full_name'], row['phone'], row['id'])
        list_of_players.append(player)
    return list_of_players


def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        found = results[0]
        player = Player(found['full_name'], found['phone'], found['id'])
    return player

def update(player):
    sql = "UPDATE players SET (full_name, phone) = (%s, %s) WHERE id = %s"
    values = [player.full_name, player.phone, player.id]
    run_sql(sql, values)
    
def players_per_campaign(campaign_id):
    party = []

    sql = "SELECT players.* FROM players INNER JOIN players_history ON players_history.player_id = players.id WHERE campaign_id = %s"
    values = [campaign_id]
    results = run_sql(sql, values)

    for row in results:
        party_member = Player(row['full_name'], row['phone'], row['id'])
        party.append(party_member)

    return party


def availability(campaign):
    lenght = len(players_per_campaign(campaign.id))
    if lenght < campaign.max_capacity:
        return True
    else:
        return False