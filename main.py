
from sum_guess_game import Game
from basic_player import Player
from bisect_player import Player




def do_game_simu(p1_cl, p2_cl, n, simu_n):
    """Simulate a game with choice bound n between two players
        @param p1_cl: Class of player 1
        @param p2_cl: Class of player 2
        @param n: Upper bound for the number to choose
        @param simu_n: How many times to run the simulation

        @returns: Player winning fractions as tuple
    """
    game = Game(n)
    game.set_players(p1_cl(n), p2_cl(n))
    wins = [0, 0]
    for i in range(simu_n):
        game.play_game()
        wins[game.get_index_of_winner()] += 1
    return tuple(float(w)/simu_n for w in wins)


if __name__ == "__main__":
    win_fracs = do_game_simu(Player, Player, 100, 1000)
    print (win_fracs)
