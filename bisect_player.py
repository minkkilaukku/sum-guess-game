
from basic_player import Player


class BisectPlayer(Player):
    """Guesses the middle of current limits. Choosing is kept random."""
    
    def get_guess(self, limits, situ):
        return (limits[0]+limits[1])//2
