# Copyright 2014 Dustin Wehr
# Distributed under the terms of the GNU General Public License.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""
ConsoleController: User interface for manually solving Anne Hoy's problems 
from the console.

move: Apply one move to the given model, and print any error message 
to the console. 
"""
import sys # I am importing this just so I can have a way to terminate the program when user enters 'Finish'.
from TOAHModel import TOAHModel, Cheese, IllegalMoveError

def move(model: TOAHModel, origin: int, dest: int):
    '''
    Module method to apply one move to the given model, and print any
    error message to the console. 
    
    model - the TOAHModel that you want to modify
    origin - the stool number (indexing from 0!) of the cheese you want 
             to move
    dest - the stool number that you want to move the top cheese 
            on stool origin onto.
    >>> M = TOAHModel(4)
    >>> M.fill_first_stool(5)
    >>> M.move(0,2)
    >>> M.get_move_seq()
    MoveSequence([(0, 2)])
    >>> M1 = TOAHModel(4)
    >>> M1.fill_first_stool(5)
    >>> M1.move(0,2)
    >>> M1.move(2,1)
    >>> M1.get_move_seq()
    MoveSequence([(0, 2), (2, 1)])
    '''   
    has_cheese = False
    length_of_dest_stool = len(model.stools[dest])
    if length_of_dest_stool > 0:
        has_cheese = True
    if has_cheese and model.top_cheese(origin).size > model.top_cheese(dest).size:
        raise IllegalMoveError('Illegal move, try again!')
    else:
        relocate = model.stools[origin].pop()
        model.stools[dest].append(relocate)
        model.move_count += 1
        moves_tup = (origin,dest)
        model._move_seq.append(moves_tup)      


class ConsoleController:
    
    def __init__(self: 'ConsoleController', 
                 number_of_cheeses: int, number_of_stools: int):
        """
        Initialize a new 'ConsoleController'.

        number_of_cheeses - number of cheese to tower on the first stool                            
        number_of_stools - number of stools
        """
        self.number_of_cheeses = number_of_cheeses
        self.number_of_stools = number_of_stools
                
    def play_loop(self: 'ConsoleController'):
        '''    
        Console-based game. 
        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the specifications given in your instruction or if it denotes
        an invalid move (e.g. moving a cheese onto a smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've 
        provided to print a representation of the current state of the game.
        '''
        current_move = 0
        origin = ''
        dest = ''
        print(m5)
        while origin != 'Finish' and dest != 'Finish':
            print("Enter origin stool (stool you want to move cheese from - the first stool is 0 and the last stool is 3):")
            origin = input()
            if origin == 'Finish':
                break            
            print("Enter destination stool (stool you want cheese to go to - the first stool is 0 and the last stool is 3):")
            dest = input()
            if dest == 'Finish':
                break            
            try:
                move(m5, int(origin), int(dest))
                current_move += 1
            except Exception:
                print ('INVALID INPUT(S)...Please try again')
            print(m5)
            print("Total moves so far: " + str(current_move))


if __name__ == '__main__':
    # TODO: 
    # You should initiate game play here. Your game should be playable by
    # running this file.    
    print('=========================================================================')
    print("You have 4 stools to play the game, as per assignment instructions") 
    print("This assignment says that only four stools are allowed")
    print("Follow the instructions or type 'Finish' to quit the session")   
    print('=========================================================================')
    print("However, please choose how many cheeses you want on your stool: ")
    how_many_cheeses = input()
    if how_many_cheeses == 'Finish':
        print('Thanks for playing! ')
        sys.exit('You have chosen to exit the program. Bye!')
    
    while how_many_cheeses.isdigit() == False or int(how_many_cheeses) <= 0:
        print("Please enter a numeral value that is greater than 0")
        how_many_cheeses = input()
    try:
        how_many_cheeses = int(how_many_cheeses)
    except:
        print('Bad input, try again!')
        how_many_cheeses = int(input())

        
            
    c1 = ConsoleController(how_many_cheeses,4)
    m5 = TOAHModel(c1.number_of_stools)
    m5.fill_first_stool(c1.number_of_cheeses)
    c1.play_loop()
    print('======================================================================')
    print('Below are the moves you made:')
    print(m5.get_move_seq())
    x = m5.get_move_seq()
    print("Total moves made: "+str(x.length()))
    print("Play again soon!")
    print('======================================================================')

