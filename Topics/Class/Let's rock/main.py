# start a RockBand here
class RockBand:
    genre = "rock"
    key_instruments = ["electric guitar", "drums"]
    n_members = 4
    
    def print_a(self):
        print(self.genre)
        print(self.n_members)
        print(self.key_instruments)
    
    
beatles = RockBand()
beatles.print_a()
