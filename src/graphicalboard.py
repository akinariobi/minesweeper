#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`graphicalboard` module

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date:  2015, september, last revision: 2017, september

This module implements some functions to draw a minesweeper game. The
graphical board uses buttons to draw each cell and maps the left-click
and right-click events to interact with the minesweeper.

This module uses from :mod:`minesweeper`:

* :method:`Minesweeper.get_width`
* :method:`Minesweeper.get_height`
* :method:`Minesweeper.get_cell`
* :method:`Minesweeper.reveal_all_cells_from`
* :method:`Minesweeper.get_state`

and from :mod:`cell`
* :method:`Cell.set_hypothetic`
* :method:`Cell.unset_hypothetic`
* :method:`Cell.is_bomb`
* :method:`Cell.is_hypothetic_bomb`
* :method:`Cell.is_revealed`

To draw and run a minesweeper game, one has to:

* create a minesweeper game g
* create a graphical board from the minesweeper g

"""

import os
import tkinter as tk
from functools import partial
from cell import Cell
from minesweeper import *

# the list of icons
img = []

def create(game):
    """
    This function creates the graphical board from a game. It also
    launches the event loop. Thus, this is the only function to run to
    have a functional graphical board.

    :param game: the minesweeper game
    :type game: Minesweeper
    :return: None
    """
    global img
    # create a new Tk window
    win = tk.Tk()
    # define the window title
    win.title('Minesweeper ({:d} bombs)'.format(game.get_nbombs()))
    # load images
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
    img = [
        tk.PhotoImage(file=os.path.join(iconpath, "0.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "1.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "2.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "3.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "4.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "5.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "6.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "7.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "8.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "9.gif")),  # unrevealed
        tk.PhotoImage(file=os.path.join(iconpath, "10.gif")), # bomb explosed
        tk.PhotoImage(file=os.path.join(iconpath, "11.gif")), # bomb discovered
        tk.PhotoImage(file=os.path.join(iconpath, "12.gif")), # flag
        tk.PhotoImage(file=os.path.join(iconpath, "13.gif"))  # question
    ]
    # create the graphical board made of Tk buttons
    width, height = (game.get_width(), game.get_height())
    board = []
    for i in range(width):
        board.insert(i, [])
        for j in range(height):
            button = tk.Button(win, padx=0, pady=0, width=19, height=19, image=img[9])
            button.grid(column=i, row=j)
            board[i].insert(j, button)
            # bind the right-click event
            button.bind("<Button-3>", partial(__changeflag, board=board, game=game, x=i, y=j))
            # bind the left-click event
            button.config(command=partial(__changestate, board, game, i, j))
    # event loop
    win.mainloop()

def __test_end(board, game):
    """
    This function tests if the game is finished or not.  In the first
    case, depending on the state of the game, all graphical cells are
    diabled or events are unbinded.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type game: Minesweeper

    """
    state = game.get_state()
    if state == GameState.losing:
        __disable_game(board, game)
    elif state == GameState.winning:
        __block_game(board, game)

def __changestate(board, game, x, y):
    """
    This function is called on left-click on a button.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type g: Minesweeper
    :param x: the x-coordinate of the cell
    :type x: int
    :param y: the y-coordinate of the cell
    :type y: int
    """
    game.reveal_all_cells_from(x, y)
    __redraw(board, game, x, y)
    __test_end(board, game)

def __changeflag(evt, board, game, x, y):
    """
    This function is called on right-click on a button.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type game: Minesweeper
    :param x: the x-coordinate of the cell
    :type x: int
    :param y: the y-coordinate of the cell
    :type y: int
    """
    cel = game.get_cell(x, y)
    if not cel.is_hypothetic():
        cel.set_hypothetic()
    else:
        cel.unset_hypothetic()
    __redraw(board, game, x, y)
    __test_end(board, game)


def __block_game(board, game):
    """
    This function is called once the player wins. The chosen behavior
    is to let the board as it and to unbind events.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type game: Minesweeper

    """
    width, height = (game.get_width(), game.get_height())
    for i in range(width):
        for j in range(height):
            button = board[i][j]
            button.config(command="")
            button.bind("<Button-3>", "")

def __disable_game(board, game):
    """
    This function is called once the player looses. The chosen behavior
    is to shade the board and to unbind events.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type game: Minesweeper

    """
    width, height = (game.get_width(), game.get_height())
    for i in range(width):
        for j in range(height):
            button = board[i][j]
            button.config(state=tk.DISABLED)
            button.bind("<Button-3>", "")


def __redraw(board, game, x, y):
    """
    This function draws the board. Positions x and y are used to test
    which bomb icon has to be drawn.

    :param board: the board of buttons
    :type board: list of list of ``button``
    :param game: the minesweeper game
    :type game: game
    :param x: the x-coordinate of the cell
    :type x: int
    :param y: the y-coordinate of the cell
    :type y: int
    """
    width, height = (game.get_width(), game.get_height())
    for i in range(width):
        for j in range(height):
            cel = game.get_cell(i, j)
            button = board[i][j]
            if cel.is_revealed():
                if cel.is_bomb():
                    new_img = img[10]
                    if x == j and y == i:
                        new_img = img[11]
                else:
                    new_img = img[cel.number_of_bombs_in_neighborhood()]
                button.config(relief=tk.FLAT, image=new_img, command="")
            elif cel.is_hypothetic():
                button.config(image=img[12])
            else:
                button.config(image=img[9])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
