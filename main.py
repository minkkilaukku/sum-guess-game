
from sum_guess_game import Game
from basic_player import Player
from bisect_player import BisectPlayer
from own_know_player import OwnKnowPlayer
from edge_guess_player import EdgeGuessPlayer







if __name__ == "__main__":
    simu_n = 1000
    #game_ns = list(range(1, 11)) + [15, 25, 50, 75, 100, 250, 500, 1000] 
    game_ns = [1,2,3,4,5, 10, 25, 50, 100, 500, 1000]
    player_classes = [
        #Player,
        #BisectPlayer,
        OwnKnowPlayer,
        EdgeGuessPlayer,
                      ]
    player_names = [str(p_cl).split(".")[-1][:-2] for p_cl in player_classes]
    name_len_max = max(len(w) for w in player_names)
    results = {n: [0.0 for _ in player_classes] for n in game_ns}

    #divisor is the number of pairs
    tot = (len(player_classes)*(len(player_classes)-1))/2

    for n in game_ns:
        players_for_n = [pc(n) for pc in player_classes]
        game = Game(n)
        #play games for each pair of players both ways (first one starts)
        for i1, p1 in enumerate(players_for_n):
            for i2, p2 in enumerate(players_for_n):
                if i1==i2: continue #don't play against self
                game.set_players(p1, p2)
                wf1, wf2 = game.simulate(simu_n)
                results[n][i1] += wf1/tot
                results[n][i2] += wf2/tot     

    
    
    print ("Simulation results for simu_n = "+str(simu_n))      
    for n, res in sorted(results.items()):
        print ("Results for n = %d:\n" %n)
        for f, i in sorted(zip(res, range(len(player_classes))), reverse=True):
            #pName = str(player_classes[i]).split(".")[-1]
            print ("%s: %.5f" %(player_names[i].ljust(name_len_max), f))
        print ("\n")



    
