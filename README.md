# Minesweeper game 
A python Minesweeper

[![Collab](https://img.shields.io/badge/%E2%99%A5-collaborator-ff0068.svg)](https://github.com/MajorPetrov)
[![Wiki](https://img.shields.io/badge/wiki-minesweeper-c40050.svg)](https://en.wikipedia.org/wiki/Minesweeper_(video_game))
[![Test](https://img.shields.io/badge/test-code%20climate-890038.svg)](https://codeclimate.com/github/akinariobi/minesweeper)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/akinariobi/minesweeper.svg?columns=all)](https://waffle.io/akinariobi/minesweeper)

### Terminal version

```
$ python3 console_main.py 5 5 3
     0   1   2   3   4
  +---+---+---+---+---+
 0|   |   |   |   |   |
  +---+---+---+---+---+
 1|   |   |   |   |   |
  +---+---+---+---+---+
 2|   |   |   |   |   |
  +---+---+---+---+---+
 3|   |   |   |   |   |
  +---+---+---+---+---+
 4|   |   |   |   |   |
  +---+---+---+---+---+
Your play x,y,C (C=(R)eveal,(S)et,(U)nset): 0,0,R
     0   1   2   3   4
  +---+---+---+---+---+
 0|  1|   |   |   |   |
  +---+---+---+---+---+
 1|   |   |   |   |   |
  +---+---+---+---+---+
 2|   |   |   |   |   |
  +---+---+---+---+---+
 3|   |   |   |   |   |
  +---+---+---+---+---+
 4|   |   |   |   |   |
  +---+---+---+---+---+
Your play x,y,C (C=(R)eveal,(S)et,(U)nset): 4,4,R
     0   1   2   3   4
  +---+---+---+---+---+
 0|  1|   |   |   |   |
  +---+---+---+---+---+
 1|   |   |   |   |   |
  +---+---+---+---+---+
 2|   |   |   |   |   |
  +---+---+---+---+---+
 3|   |   |   |   |   |
  +---+---+---+---+---+
 4|   |   |   |   |  1|
  +---+---+---+---+---+
Your play x,y,C (C=(R)eveal,(S)et,(U)nset): 4,0,R
     0   1   2   3   4
  +---+---+---+---+---+
 0|  1|  1|  0|  0|  0|
  +---+---+---+---+---+
 1|   |  1|  0|  1|  1|
  +---+---+---+---+---+
 2|  1|  1|  0|  2|   |
  +---+---+---+---+---+
 3|  0|  0|  0|  2|   |
  +---+---+---+---+---+
 4|  0|  0|  0|  1|  1|
  +---+---+---+---+---+
You win !
```

### GUI version

You have to install Tkinter if you want to play GUI version

🍻🍻🍻 homebrew 🍻🍻🍻
```
$ brew install homebrew/dupes/tcl-tk
```

```
$ find . -type d | grep minesweeper
//go to minesweeper dir
$ python3 graphical_main.py 10 5 3
```
![TITLE](http://www.fil.univ-lille1.fr/~L2S3API/CoursTP/_images/minesweeper.png)

