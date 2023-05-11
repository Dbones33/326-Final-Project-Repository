# 326-Final-Project-Repository
A program that runs the boardgame, Ludo

Repository files:
The 326_Final_Project_Reposititory.py file's purpose is to brainstorm ideas in the form of pseudocode to build a skeleton for the group's final deliverable.
Ludo.py is the main file that the group worked on and make adjustments during office hours and group meetings.
.gitgnore is a file that establishes packages and functions that could be imported in python files for this repository.
LICENSE does not contribute to the repositiory since it is mainly for use of GitHub.

Running the program from the command line:
1. Type Python(3) ludo.py --load_game ludo_save.json(add the 3 if you are on a mac)
2. Input names of participating players
3. After the dice roll, type either 0, 1, 2, or 3 to move a player's piece on the board
4. (OPTIONAL) - Save the game into a ludo_save json file and end the program
5. Make sure all of one player's four pieces reach the goal to end the game

How to use the program/Interpret the output of the program:
Make sure to have a directory for the program file and the json file in case if the user wishes to save the game during execution.
Use --load_game ludo_save.json even if the user is running the program for the first time.
There should only be one winner printed at the end of the game.

Attribution:
Method/function            Primary author      Techniques demonstrated

restart                    Emmitt Anton        F-strings containing expressions
play_turn                  Emmitt Anton        List comprehension 


class Board, class Ludo    Justin Gold         Composition of two original classes 
__getitem__, __setitem__   Justin Gold         Magic methods other than init


save_game                  Sam Henderlite      Use of json.dump()
argument_parser            Sam Henderlite      The ArgumentParser class from the argparse module


load_game                  David Kneebone      With statements
bar_plot                   David Kneebone      Visualizing data with pyplot or seaborn

