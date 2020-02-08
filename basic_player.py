
import random



class Player(object):
    """An AI-player for sum guessing game.
    This basic class makes a random guess in the given limits.
    Inherit from this and implement your own AI-player.
    """
    
    def __init__(self, n):
        """Initialize a player for a game where upper limit is n."""
        self.n = n

    def get_number(self):
        """Get the choice of the player. Must be integer in the range [1, n]"""
        return random.randint(1, self.n)

    def get_guess(self, limits, situ):
        """Get a number the player guesses.
        @param limits: Array of the current bounds [low, high] where the
                       guess must be.
        @param situ: A dictionary containing information about the current
                    situation of the game.
                    Has the form
                    {
                        'guesses': [...previous guesses]
                    }
                    ###(There isn't any other information than
                    ###previous guesses but it's better to keep them in dict)
                    ###TODO: should the limits also be put there?
        """
        return random.randint(limits[0], limits[1])
    
