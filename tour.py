# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr
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
from TOAHModel import TOAHModel

import time
OFFSET = 1 # make code more readable since +-1 is used a lot. 
import math # need this in order to calculate square-root using math.sqrt()

def three_stools(model1:'TOAHModel', num_cheeses:'int', origin:'int', dest:'int', mid_stool1:'int'):
    '''
    Moves the TOAHModel model1, num_cheeses cheeses using only the three stools after it has been divided by the optimal number "i" from the origin, origin, to the destination dest using a temporary stool called mid_stool1.
    '''    
    if(num_cheeses != 0):
        three_stools(model1, num_cheeses-OFFSET, origin, mid_stool1, dest)
        model1.move(origin,dest)
        three_stools(model1,num_cheeses-OFFSET, mid_stool1, dest, origin)	

def the_four_stools(model1: 'TOAHModel', num_cheeses:'int', origin:'int', mid_stool1:'int', mid_stool2:'int', dest:'int'): # the mid_stool variables can be thought of as temporary stools. (i.e stools that are used just to move cheeses more efficiently.)
    '''
    Moves the TOAHModel model1, num_cheeses cheeses using the four stools after it has been divided by the optimal number "i" from the origin, origin, to the destination dest using a temporary stools called mid_stool1 and mid_stool2.
    '''     
    optimal_num = 0
    if (num_cheeses == 1):
        model1.move(origin,dest)
    else:
        optimal_num =((math.sqrt(8*num_cheeses+1)-1)/2)	# see source(s) above for formula
        optimal= int(optimal_num)
        the_four_stools(model1, num_cheeses-optimal, origin, mid_stool2, dest, mid_stool1)
        three_stools(model1, optimal, origin, dest, mid_stool2)
        the_four_stools(model1, num_cheeses-optimal, mid_stool1, origin, mid_stool2, dest)

'''
===========================================================================
'''
        
def tour_of_four_stools(model: TOAHModel, delay_btw_moves: float=0.5, console_animate: bool=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

       model - a TOAHModel with a tower of cheese on the first stool
                and three other empty stools
       console_animate - whether to animate the tour in the console
       delay_btw_moves - time delay between moves in seconds IF 
                         console_animate == True
                         no effect if console_animate == False
    """
    the_four_stools(model, model.number_of_cheeses(), 0, 1, 2, 3) # stool starts at 0 and ends at 3
    if console_animate == True:
	    x = model.get_move_seq()
	    z = x.length()
	    y = model.number_of_cheeses()
	    model = TOAHModel(4)
	    model.fill_first_stool(y)
	    index = 0
	    time.sleep(delay_btw_moves)
	    print(model)
	    while index < z:
		    time.sleep(delay_btw_moves)
		    m = x.get_move(index)
		    model.move(m[0],m[1])
		    time.sleep(delay_btw_moves)
		    print(model)
		    time.sleep(delay_btw_moves)
		    index += 1
		    


if __name__ == '__main__':
    NUM_CHEESES = 9
    DELAY_BETWEEN_MOVES = 0.5
    CONSOLE_ANIMATE = True
    
    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)    
    four_stools.fill_first_stool(number_of_cheeses=NUM_CHEESES)
    
    tour_of_four_stools(four_stools, 
                        console_animate=CONSOLE_ANIMATE,
                        delay_btw_moves=DELAY_BETWEEN_MOVES)
    
    print(four_stools.number_of_moves())
