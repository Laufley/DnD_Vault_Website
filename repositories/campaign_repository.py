from db.run_sql import run_sql

from models.player import Player
from models.campaign import Campaign
import repositories.player_repository as player_repository



def delete_all():
    sql = "DELETE FROM campaigns"
    run_sql(sql)

def save(campaign):
    sql = "INSERT INTO campaigns (title, genre, dm, max_capacity, price) VALUES ( %s, %s, %s, %s, %s) RETURNING *"
    values = [campaign.title, campaign.genre, campaign.dm, campaign.max_capacity, campaign.price]
    results = run_sql( sql, values )
    campaign.id = results[0]['id']
    return campaign


def select_all_campaigns():
    list_of_campaigns = []
    
    sql = "SELECT * FROM campaigns"
    results = run_sql(sql)
    for row in results:
        campaign = Campaign(row['title'], row['genre'], row['dm'], row['price'], row['id'])
        list_of_campaigns.append(campaign)
    return list_of_campaigns


def select(id):
    campaign = None
    sql = "SELECT * FROM campaigns WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        found = results[0]
        campaign = Campaign(found['title'], found['genre'], found['dm'], found['max_capacity'], found['price'], found['id'])
    return campaign

def update(campaign):
    sql = "UPDATE campaigns SET (title, genre, dm, max_capacity, price) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [campaign.title, campaign.genre, campaign.dm, campaign.max_capacity, campaign.price, campaign.id]
    run_sql(sql, values)