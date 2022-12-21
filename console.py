# import pdb
from models.campaign import Campaign
from models.player import Player
from models.player_history import Player_history

import repositories.player_repository as player_repository
import repositories.campaign_repository as campaign_repository
import repositories.player_history_repository as player_history_repository


# campaign_repository.delete_all()
# player_repository.delete_all()

# player_1 = Player("John Smith", "+447798517041")
# player_2 = Player("Duck Duckingston", "+447898517041")
# player_3 = Player("Pere Grau", "+448765638465")
# player_4 = Player("Marie Lou", "+448374619386" )
# player_5 = Player("Moss Rogers", "+448469723461")
# player_6 = Player("Paul Davis", "+447398263947")
# player_repository.save(player_1)
# player_repository.save(player_2)
# player_repository.save(player_3)
# player_repository.save(player_4)
# player_repository.save(player_5)
# player_repository.save(player_6)


# campaign_1 = Campaign("Quest for Kaladesh", "Adventure", "Steve", 5, 15, "inspired in a long-time classic", "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/2/29/Kaladesh_art.jpg")
# campaign_2 = Campaign("Eberron's collapse", "Fanasty", "Octavio", 6, 20, "inspired in D&D", "https://flyinglizardstudio.com/wp-content/uploads/2018/02/ToA-E2.jpg")
# campaign_3 = Campaign("God save the... Djin(?)", "Fantasy", "Sophie", 4, 10, "unnexpected twists", "https://static.wikia.nocookie.net/mana/images/7/79/Jinn_%28Children_of_Mana%29.png")
# campaign_4 = Campaign("Zombies, Why not", "apocaliptic", "Steve", 8, 20, "it's fun!", "https://images.fineartamerica.com/images/artworkimages/mediumlarge/3/2-zombies-eat-brains-dont-worry-youre-safe-funny-the-perfect-presents.jpg")
# campaign_5 = Campaign("Who killed father Toad?", "mystery", "Eva", 6, 15, "if you like frogs and mistery, this is for you", "https://i.etsystatic.com/23664421/r/il/f86f67/4247540905/il_570xN.4247540905_5y7j.jpg")
# campaign_repository.save(campaign_1)
# campaign_repository.save(campaign_2)
# campaign_repository.save(campaign_3)
# campaign_repository.save(campaign_4)
# campaign_repository.save(campaign_5)

# joint_1 = Player_history(player_2, campaign_1)
# player_history_repository.save(joint_1)

# player_repository.select_all_players()
# campaign_repository.select_all_campaigns()
# player_history_repository.select_all()


# player_3 = player_repository.select(2)
# player_3.full_name = "Dan"
# player_repository.update(player_3)

# campaign_3 = campaign_repository.select(2)
# campaign_3.title = "Project Zomboid"
# campaign_repository.update(campaign_3)

# pdb.set_trace()