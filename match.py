import time

from game import Game

################################################################
#### Edit the players you wish to hold a match against here ####
#### Just change the filename before "from", nothing else   ####
################################################################
from random_player import player as player1
from mean_player import player as player2

############################################################################
#### Change the setttings for the match you wish the bots to play       ####
#### The ones present in the repo will be used in the actual tournament ####
############################################################################
point_count = 2048
max_coord = 10
rounds_in_match = 50



def play(p1, p2):
    game = Game(point_count, max_coord)
    
    time1 = 0
    score1 = 0

    time2 = 0
    score2 = 0

    for i in range(0, rounds_in_match):

        t = time.perf_counter_ns()
        ans1 = p1.think(game.points)
        time1 += time.perf_counter_ns() - t
        score1 += game.choose(ans1)

        t = time.perf_counter_ns()
        ans2 = p2.think(game.points)
        time2 += time.perf_counter_ns() - t
        score2 += game.choose(ans2)

    return (time1, score1, time2, score2)


(time1, score1, time2, score2) = play(player1, player2)

print(player1.name, "took", time1, "nanoseconds, and gathered", score1, "points")
print(player2.name, "took", time2, "nanoseconds, and gathered", score2, "points")
