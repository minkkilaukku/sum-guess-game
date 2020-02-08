from basic_player import Player
import random



class OwnKnowPlayer(Player):

    def __init__(self, n):
        super(OwnKnowPlayer, self).__init__(n)
        self.own_choice = 0

    def get_number(self):
        
        self.own_choice = random.randint(1, self.n)
        return self.own_choice
        

    def get_guess(self, limits, situ):
        low = max(self.own_choice+1, limits[0])
        high = min(self.own_choice+self.n, limits[1])
        return random.randint(low, high)




if __name__ == "__main__":
    p = OwnKnowPlayer(5)
    print (p.get_number())
    print (p.own_choice)
    print (p.get_guess([1, 10], {'guesses': []}))

