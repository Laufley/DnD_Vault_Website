# import pdb
from models.campaign import Campaign
from models.player import Player
from models.player_history import Player_history

import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository
import repositories.player_history_repository as player_history_repository


campaign_repository.delete_all()
player_repository.delete_all()

player_1 = Player("John Smith", "+447798517041")
player_repository.save(player_1)

player_2 = Player("Ian Boyd", "+447898517041")
player_repository.save(player_2)


campaign_1 = Campaign("Quest for Kaladesh", "fanasty", "Steve",  6, 15, "inspired in the MTG universe")
campaign_repository.save(campaign_1)

campaign_2= Campaign("Quest for Camelot", "Adventure", "Fred",  8, 15, "inspired in a long-time classic" )
campaign_repository.save(campaign_2)

joint_1 = Player_history(player_2, campaign_1)
player_history_repository.save(joint_1)

player_repository.select_all_players()
campaign_repository.select_all_campaigns()
player_history_repository.select_all()


# player_3 = player_repository.select(2)
# player_3.full_name = "Dan"
# player_repository.update(player_3)

# campaign_3 = campaign_repository.select(2)
# campaign_3.title = "Project Zomboid"
# campaign_repository.update(campaign_3)

# pdb.set_trace()