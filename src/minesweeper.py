#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`minesweeper` module

:author: SHCHERBAKOVA IULIIA

:date:  

This module provides functions and a class for minesweeper's game's management.

"""

import random
from enum import Enum
from cell import Cell


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Function for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :param height: height of the grid
    :type height: int
    :param width: widthof the grid
    :type width: int
    :return: the list of coordinates of the neighbors of position (x,y) in a
             grid of size width*height
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    """
    neighbors = []
    for i in range(x-1, x+2) :
        for j in range(y-1, y+2) :
            if 0<=i<width and 0<=j<height  and not (i,j)==(x,y):
                neighbors = neighbors + [ (i,j) ]
    return neighbors


def make_grid(width, height, nbombs):
    """
    return a minesweeper grid of size width*height cells
    with nbombs bombs.

    :param width: horizontal size of game (default = 30)
    :type width: int
    :param height:  vertical size of game (default = 20)
    :type height: int
    :param nbombs:  number of bombs (default = 99)
    :type nbombs: int
    :return: a fresh grid of  width*height cells
    :rtype: list of list of cells
    """
    assert 0 < width, 'width must be a positive integer'
    assert 0 < height, 'height must be a positive integer'
    assert 0 <= nbombs <= width * height, "nbombs must don't exceed width*height"
    coords = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(coords)
    grid = [[Cell() for y in range(height)] for x in range(width)]
    for i in range(nbombs):
        x,y=coords[i]
        grid[x][y].set_bomb()
        for neighbor in neighborhood(x, y, width, height):
            x1, y1 = neighbor
            grid[x1][y1].incr_number_of_bombs_in_neighborhood()
    return grid

class Minesweeper():
    """
    >>> game = Minesweeper(20, 10, 4)
    >>> game.get_width()
    20
    >>> game.get_height()
    10
    >>> game.get_nbombs()
    4
    >>> game.get_state() == GameState.unfinished 
    True
    >>> cel = game.get_cell(1, 2)
    >>> cel.is_revealed()
    False
    >>> 
    """

    def __init__(self, width=30, height=20, nbombs=99):
        """
        build a minesweeper grid of size width*height cells
        with nbombs bombs randomly placed.  

        :param width:[optional] horizontal size of game (default = 30)
        :type width: int
        :param height: [optional] vertical size of game (default = 20)
        :type height: int
        :param nbombs: [optional] number of bombs (default = 99)
        :type nbombs: int
        :return: a fresh grid of  width*height cells with nbombs bombs randomly placed.
        :rtype: Minesweeper
        :UC: width and height must be positive integers, and
             nbombs <= width * height
        :Example:

        >>> game = Minesweeper(20, 10, 4)
        >>> game.get_width()
        20
        >>> game.get_height()
        10
        >>> game.get_nbombs()
        4
        >>> game.get_state() == GameState.unfinished 
        True
        """
        self.w = width
        self.h = height
        self.nb = nbombs
        self.grid = make_grid(width, height, nbombs)
        

    def get_height(self):
        """
        :return: height of the grid in self
        :rtype: int
        :UC: none
        """
        return self.h


    def get_width(self):
        """
        :return: width of the grid in game
        :rtype: int
        :UC: none
        """
        return self.w
    
    def get_nbombs(self):
        """
        :return: number of bombs in game
        :rtype: int
        :UC: none
        """
        return self.nb


    def get_cell(self, x, y):
        """
        :param x: x-coordinate of a cell
        :type x: int
        :param y: y-coordinate of a cell
        :type y: int
        :return: the cell of coordinates (x,y) in the game's grid
        :type: cell
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        return self.grid[x][y]
        

    def get_state(self):
        """
        :return: the state of the game (winning, losing or unfinished)
        :rtype: GameState
        :UC: none
        """
        n = 0
        state = 0
        width = self.w
        height = self.h
        nb_cases = width*height
        
        for i in range(0,width) :
            for j in range(0,height) :
                cel = self.get_cell(i,j)
                if cel.is_bomb() and cel.is_revealed():
                    state = 2
                    break
                elif (cel.is_revealed() and not cel.is_bomb()) or (not cel.is_revealed() and cel.is_bomb()):
                    n = n+1
            if state == 2:
                break
        
        if n == nb_cases:
            return GameState.winning
        elif state == 2:
            return GameState.losing
        else:
            return GameState.unfinished

    def reveal_all_cells_from(self, x, y):
        """
        :param x: x-coordinate
        :param y: y-coordinate
        :return: none
        :side effect: reveal all cells of game game from the initial cell (x,y).
        :UC: 0 <= x < width of game and O <= y < height of game
        """
        width = self.w
        height = self.h
        cel = self.get_cell(x,y)
        if cel.number_of_bombs_in_neighborhood() != 0:
            cel.reveal()
        elif cel.is_bomb():
            cel.reveal()
        else:
            listeVoisins = neighborhood(x, y, width, height)
            for i in range(0,len(listeVoisins)) :
                cel2=self.get_cell(listeVoisins[i][0],listeVoisins[i][1])
                if cel2.is_revealed()==False:
                    cel2.reveal()
                    self.reveal_all_cells_from(listeVoisins[i][0], listeVoisins[i][1])


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)



