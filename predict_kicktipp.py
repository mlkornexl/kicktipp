from random import randrange

team_1 = input("Team 1:")
team_2 = input("Team 2:")

print("%s vs. %s\n\t%d:%d" % (team_1, team_2, randrange(0, 3), randrange(0, 3)))

