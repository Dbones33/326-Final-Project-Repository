# 326-Final-Project-Repository
A program that runs the boardgame, Ludo

Repository files:
The 326_Final_Project_Reposititory.py file's purpose is to brainstorm ideas in the form of pseudocode to build a skeleton for the group's final deliverable.
Ludo.py is the main file that the group worked on and make adjustments during office hours and group meetings.
.gitgnore is a file that establishes packages and functions that could be imported in python files for this repository.
LICENSE does not contribute to the repository since it is mainly for use of GitHub.

Running the program from the command line:
1. Type Python(add 3 if you are on mac) ludo.py 
(OPTIONAL) --load_game with the path to a saved JSON file after it, --player1_name with a name in a string after it to rename player1, --player2_name with a name in a string after it to rename player2
2. After the dice roll, type either 0, 1, 2, or 3 to move a player's piece on the board
3. You will be asked if you want to save the game. Type 'n' if you want to keep playing
4. (OPTIONAL) - Choose 'y' when prompted if you want to save the game. Then a prompt will ask where you want to save the file to. Type in the name of a JSON filepath you want to save the game to.
5. Make sure all of one player's four pieces reach the goal to end the game

How to use the program/Interpret the output of the program:
Make sure to have a directory for the program file and the json file in case if the user wishes to save the game during execution.
There should only be one winner printed at the end of the game.

Attribution:
Method/function                      Primary author      Techniques demonstrated

restart                              Emmitt Anton        F-strings containing expressions
play_turn                            Emmitt Anton        List comprehension 


class Board, class Ludo              Justin Gold         Composition of two original classes 
__getitem__, __setitem__, __repr__   Justin Gold         Magic methods other than init


save_game                            Sam Henderlite      Use of json.dump()
argument_parser                      Sam Henderlite      The ArgumentParser class from the argparse module


load_game                            David Kneebone      With statements
bar_plot                             David Kneebone      Visualizing data with pyplot or seaborn

