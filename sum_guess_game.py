
from basic_player import Player


class Game():
    """A two player game, where each player first chooses
    an integer from the interval [1, n]. These choices are kept secret.
    Then the player start to turn by turn guess the sum of the two numbers
    they chose. After every guess it is announced whether the guess was
    too low or too high (if it wasn't correct). The next guess must be on
    the possible interval given the limits. Player to first guess the correct
    sum is the winner. If a player makes a nonsense guess (not in the current
    bounds or not an integer), the other player wins immediately.
    Also, if the number chosen by a player isn't in the bounds [1, n],
    this leads to disqualification and the other player wins.

    Example game with n = 100

    Player 1 chooses x1 = 42
    Player 2 chooses x2 = 71
    The sum is S = x1 + x2 = 113

    Player 1 starts the guessing.
    The limits are [2, 200]
    Player 1 guesses 95
    Too low.
    The limits become [96, 200]
    Player 2 guesses 150
    Too high.
    The limits become [96, 149]
    Player 1 guesses 96
    Too low.
    The limits become [97, 149]
    Player 2 guesses 125
    Too high, the limits become [97, 124]
    Player 1 guesses 111
    Too low. The limits become [112, 124]
    Player 2 guesses 119
    Too high, the limits become [112, 118]
    Player 1 guesses 113
    Correct!
    Player 1 wins.
    """

    def __init__(self, n):
        """Make a new game with choice bound n"""
        self.n = n
        self.players = []
        self.turn = 0
        self.limits = [2, 2*self.n]
        self.S = 0
        self.winner = None
        self.situ = {'guesses': []}

    def set_players(self, p1, p2):
        self.players = [p1, p2]

    def init_game(self, log=False):
        self.turn = 0
        self.limits = [2, 2*self.n]
        self.situ['guesses'] = []
        self.winner = None
        self.S = 0
        for i, p in enumerate(self.players):
            c = p.get_number()
            cIsOk = type(c)==int and c>=1 and c<=self.n
            if log:
                print ("Player %d chooses %s" %(i, str(c)))
            if not cIsOk:
                self.winner = self.players[(i+1)%2] #2 players
                if log:
                    print ("Choice isn't OK!!")
                break
            self.S += c
        #self.S = sum(p.get_number() for p in self.players)

    def play_turn(self, log=False):
        p = self.players[self.turn]
        g = p.get_guess(self.limits, self.situ)
        if log:
            print ("Guesses so far is %s" %(self.situ['guesses']))
            print ("Player %d guesses %s." %(self.turn, str(g)))
        gIsOk = type(g)==int and g>=self.limits[0] and g<=self.limits[1]
        if not gIsOk:
            #other player wins if current makes nonsense guess
            self.winner = self.players[(self.turn+1)%2] #2 players
            if log:
                print ("Guess isn't OK!!")
        elif g==self.S:
            self.winner = p
            if log:
                print ("Guess is correct!")
        elif g<self.S:
            self.limits[0] = g+1
            if log:
                print ("Guess is too low")
        else: # g>self.S
            self.limits[1] = g-1
            if log:
                print ("Guess is too high")

        if gIsOk and g!=self.S:
            if log:
                print ("Limits are [%d, %d]" %(self.limits[0], self.limits[1]))

        if gIsOk:
            self.situ['guesses'].append(g)
        
    def play_game(self, log=False):
        if log:
            print ("Game begins")
        self.init_game(log=log)
        if log:
            print ("Limits are [%d, %d]" %(self.limits[0], self.limits[1]))
        while not self.winner:
            self.play_turn(log=log)
            if self.winner: break
            self.turn = (self.turn+1)%len(self.players)
        if log:
            print ("Player %d wins." %(self.turn,))

    def get_index_of_winner(self):
        if self.winner in self.players: return self.players.index(self.winner)
        else: return -1


    def simulate(self, simu_n):
        """Play the game multiple times and return the winning fractions
        @param simu_n: how many times to play the game.
        @return A tuple of players winning fractions"""
        wins = [0, 0]
        for i in range(simu_n):
            self.play_game(False)
            wins[self.get_index_of_winner()] += 1
        return tuple(float(w)/simu_n for w in wins)

if __name__ == "__main__":
    from bisect_player import BisectPlayer
    n = 100
    g = Game(n)
    g.set_players(BisectPlayer(n), Player(n))
    g.play_game(1)
    print ("Winner is player at index %d" %g.players.index(g.winner))

        
        
