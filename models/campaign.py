class Campaign:
    def __init__(self, title, genre, dm, max_capacity, price, id= None):
        self.title = title
        self.genre = genre
        self.dm = dm
        self.max_capacity = max_capacity
        self.price = price
        self.id = id
        
        
    def add_player(self, player):
        self.party_members.append(player)    
        
    def number_of_players(self):        
        return len(self.party_members)
    
    def availability(self):
        number_of_requests = int(self.number_of_players())
        if number_of_requests < self.max_capacity:
            return True
        else:
            return False
        
    def substract_player(self, player):
        self.party_members.remove(player)

    def book_player(self, player): 
        if self.availability() == True:
            self.add_player(player)
            return player     
        else:
            return f"Oops! Our party is full, {player.full_name}. Try another!"
    
    def unbook_player(self, player): 
        if player in self.party_members:
            self.substract_player(player)
            return f"Thanks for coming, {player.full_name}. Please join us again!"
        else:
            return f"Error, try again later"
        
