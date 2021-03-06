from django.db import models

# Create your models here.

class player(models.Model):
    x = 1
    y = 0
    o = 'S'
    
    def __unicode__(self):
        return "Position: %d : %d Orientation: %s" % (self.x, self.y, self.o)


class labyrinth(models.Model):
    labyrinthPath = """
0100
0100
0110
00E0
"""
    labyrinthPath = """
0100000000000
0110111101000
0010000101000
0111111101000
0010000111000
0010100100011
0011111100010
0000100100010
0100100111110
0111110100000
0100000E00000
0000000000000
"""


    labyrinth = []

    def __init__(self):
        tmpLabyrinth = self.labyrinthPath.splitlines()
        tmpLabyrinth.remove('')
        for row in tmpLabyrinth:
            self.labyrinth.append(list(row))
    
    def checkMove(self, player, move):
        if player.o == 'N':
            if move == 'V':
                player.y = player.y - 1
            elif move == 'R':
                player.x = player.x + 1
                player.o = 'O'
            elif move == 'L':
                player.x = player.x - 1
                player.o = 'W'
            elif move == 'H':
                player.y = player.y + 1
                player.o = 'S'
        elif player.o == 'O':
            if move == 'V':
                player.x = player.x + 1
            elif move == 'R':
                player.y = player.y + 1
                player.o = 'S'
            elif move == 'L':
                player.o = 'N'
                player.y = player.y - 1
            elif move == 'H':
                player.o = 'W'
                player.x = player.x - 1
        elif player.o == 'S':
            if move == 'V':
                player.y = player.y + 1
            elif move == 'R':
                player.x = player.x - 1
                player.o = 'W'
            elif move == 'L':
                player.o = 'O'
                player.x = player.x + 1
            elif move == 'H':
                player.o = 'N'
                player.y = player.y - 1
        elif player.o == 'W':
            if move == 'V':
                player.x = player.x - 1
            elif move == 'R':
                player.o = 'N'
                player.y = player.y - 1
            elif move == 'L':
                player.o = 'S'
                player.y = player.y + 1
            elif move == 'H':
                player.o = 'O'
                player.y = player.x + 1
        
        return self.labyrinth[player.y][player.x]
    
    def __unicode__(self):
        return self.labyrinthPath