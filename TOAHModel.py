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
"""
TOAHModel:  Model a game of Towers of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will 
need to return MoveSequence object after solving an instance of the 4-stool 
Towers of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""


class TOAHModel:
    """Model a game of Towers Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.

    fill_first_stool - put an existing model in the standard starting config
    move - move cheese from one stool to another
    add - add a cheese to a stool        
    top_cheese - top cheese on a non-empty stool    
    cheese_location - index of the stool that the given cheese is on
    number_of_cheeses - number of cheeses in this game
    number_of_moves - number of moves so far
    number_of_stools - number of stools in this game
    get_move_seq - MoveSequence object that records the moves used so far
     
    """

    # My Constructor
    
    def __init__(self: 'TOAHModel', number_of_stools: 'int'):
        '''
        Initializes a TOAHModel object.
        
        number_of_stools - the number of stools that the TOAHModel object has. 
        '''
        self.stools = []
        self._move_seq = []
        self.num_cheeses = 0
        self.num_stools = number_of_stools 
        self.move_count = 0
        chairs = 0
        while chairs < number_of_stools:
            self.stools.append([])
            chairs += 1
            
    def number_of_cheeses(self: 'TOAHModel') -> int:
        '''
        Returns the number of cheeses in TOAHModel.
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(10)
        >>> M.number_of_cheeses()
        10
        >>> M1 = TOAHModel(10000)
        >>> M1.fill_first_stool(10000)
        >>> M1.number_of_cheeses()
        10000
        '''
        return self.num_cheeses      
        
    def number_of_stools(self: 'TOAHModel') -> int:
        '''
        Returns the number of stools in the TOAHModel object. 
        >>> M = TOAHModel(4)
        >>> M.number_of_stools()
        4
        >>> M1 = TOAHModel(10000)
        >>> M1.number_of_stools()
        10000
        '''
        return self.num_stools            
     
    def move(self: 'TOAHModel', origin_stool: int, dest_stool: int):
        '''
        Move the cheese from origin_stool stool to dest_stool stool.
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
        length_of_dest_stool = len(self.stools[dest_stool])
        if length_of_dest_stool > 0:
            has_cheese = True
        if has_cheese and self.top_cheese(origin_stool).size > self.top_cheese(dest_stool).size:
            raise IllegalMoveError('Illegal move, try again!')
        else:
            relocate = self.stools[origin_stool].pop()
            self.stools[dest_stool].append(relocate)
            self.move_count += 1
            moves_tup = (origin_stool,dest_stool)
            self._move_seq.append(moves_tup) 
            
                       
    def cheese_location(self: 'TOAHModel', cheese: 'Cheese') -> int:
        '''
        Index of the stool that the given cheese, cheese is on
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.cheese_location(Cheese(4))
        0
        >>> M1 = TOAHModel(4)
        >>> M1.fill_first_stool(3)
        >>> M1.move(0,2)
        >>> M1.cheese_location(Cheese(1))
        2
        '''
        x = cheese
        total_stools = self.number_of_stools()
        chair = 0
        while chair < total_stools:
            cheese_num = len(self.stools[chair])-1
            possible = 0
            while possible <= cheese_num:
                if x == self.stools[chair][cheese_num]:
                    return chair
                cheese_num -= 1
            chair += 1        

    def top_cheese(self: 'TOAHModel', stool_index: int) -> 'Cheese':
        '''
        Returns the top cheese on stool_index which is a non empty stool 
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.top_cheese(0)
        Cheese(1)
        >>> M1 = TOAHModel(4)
        >>> M1.fill_first_stool(3)
        >>> M1.move(0,1)
        >>> M1.top_cheese(0)
        Cheese(2)
        '''
        has_cheese = False
        if len(self.stools[stool_index]) != 0:
            has_cheese = True
        if has_cheese == True:
            return self.stools[stool_index][len(self.stools[stool_index])-1]
        else:
            return None
        
    def add(self: 'TOAHModel', stool_index: int, cheese: 'Cheese'):
        '''
        This method is used by GUIController only during initialization with a
        hard-coded value for stool index 0. Comparitive to fill_first_stool.
        >>> M = TOAHModel(4)
        >>> M.add(0,Cheese(1))
        >>> print(M.stools)
        [[Cheese(1)], [], [], []]
        >>> M1 = TOAHModel(4)
        >>> M1.add(0,Cheese(4))
        >>> print(M1.stools)
        [[Cheese(4)], [], [], []]
        '''        
        self.stools[stool_index].append(cheese)
    
    def number_of_moves(self: 'TOAHModel') -> int:
        """
        Record the number of moves that it takes to move cheeses from various stools
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(3)
        >>> M.move(0,3)
        >>> M.number_of_moves()
        1
        >>> M1 = TOAHModel(4)
        >>> M1.fill_first_stool(7)
        >>> M1.move(0,1)
        >>> M1.move(1,2)
        >>> M1.move(0,3)
        >>> M1.number_of_moves()
        3
        """
        return self.move_count
    
    def fill_first_stool(self: 'TOAHModel', number_of_cheeses: int):
        """
        Put number_of_cheeses cheeses on the first (i.e. 0-th) stool, in order 
        of size, with a cheese of size == number_of_cheeses on bottom and 
        a cheese of size == 1 on top.      
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> print(M.stools)
        [[Cheese(5), Cheese(4), Cheese(3), Cheese(2), Cheese(1)], [], [], []]
        >>> M1 = TOAHModel(4)
        >>> M1.fill_first_stool(3)
        >>> print(M1.stools)
        [[Cheese(3), Cheese(2), Cheese(1)], [], [], []]
        """
        # Using a list as a stack where first element is biggest cheese and last
        # element is smallest cheese
        self.num_cheeses = number_of_cheeses
        stool_zero = 0
        index = 0
        total = number_of_cheeses
        while total > index:
            self.stools[stool_zero].append(Cheese(total))
            total -= 1
                  

    def _cheese_at(self: 'TOAHModel', stool_index, 
                   stool_height: int) -> 'Cheese':
        """
        If there are at least stool_height+1 cheeses 
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.
        
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._cheese_at(0,3).size
        2
        >>> M._cheese_at(0,0).size
        5
        """
        try:
            return self.stools[stool_index][stool_height]
        except Exception:
            return None

    def get_move_seq(self: 'TOAHModel') -> 'MoveSequence':
        """
        If there are at least stool_height+1 cheeses 
        on stool stool_index then return the (stool_height)-th one.
        Otherwise return None.
        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M.move(0,2)
        >>> M.get_move_seq()
        MoveSequence([(0, 2)])
        >>> M1 = TOAHModel(4)
        >>> M1.fill_first_stool(5)
        >>> M1.move(0,2)
        >>> M1.move(0,1)
        >>> M1.get_move_seq()
        MoveSequence([(0, 2), (0, 1)])
        """        
        rec = MoveSequence(self._move_seq)
        return rec   
                
    def __eq__(self: 'TOAHModel', other: 'TOAHModel') -> bool:
        """
        We're saying two TOAHModels are equivalent if their current 
        configurations of cheeses on stools look the same. 
        More precisely, for all h,s, the h-th cheese on the s-th 
        stool of self should be equivalent the h-th cheese on the s-th 
        stool of other
        
        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0,1)
        >>> m1.move(0,2)
        >>> m1.move(1,2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0,3)
        >>> m2.move(0,2)
        >>> m2.move(3,2)
        >>> m1 == m2
        True
        """
        pre_index = 0
        if self.number_of_stools() != other.number_of_stools():
            return False        
        if self.number_of_cheeses() != other.number_of_cheeses():
            return False
        while pre_index < self.number_of_stools():
            if len(self.stools[pre_index]) != len(other.stools[pre_index]):
                return False   
            pre_index += 1
        index = 0 
        count = 0
        while index < self.number_of_stools():
            while count < len(self.stools[index]):
                if self.stools[index][count] != other.stools[index][count]:
                    return False
                count += 1
            index += 1
        return True
        
    def __str__(self: 'TOAHModel') -> str:       
        """
        Depicts only the current state of the stools and cheese.
        """
        stool_str = "=" * (2 * (self.number_of_cheeses()) + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.number_of_stools()
        
        def cheese_str(size: int):            
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler
        
        lines = ""
        for height in range(self.number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = cheese_str(int(c.size))
                else:
                    s = cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str
        
        return lines
    
    
class Cheese:
    def __init__(self: 'Cheese', size: int):
        """
        Initialize a Cheese to diameter size.

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __repr__(self: 'Cheese') -> str:
        """
        Representation of this Cheese
        """
        return "Cheese(" + str(self.size) + ")"

    def __eq__(self: 'Cheese', other: 'Cheese') -> bool:
        """Is self equivalent to other? We say they are if they're the same 
        size."""
        return isinstance(other, Cheese) and self.size == other.size
    
       
class IllegalMoveError(Exception):
    pass

#class Stool:
    #def __init__(self: 'Stool'):
        #self.cheeses = []
        
    #def place_cheese_on_stool(self: 'Stool', cheese: 'Cheese'):
        #self.cheeses.append(cheese)

class MoveSequence:
    def __init__(self: 'MoveSequence', moves: list):
        # moves - a list of integer pairs, e.g. [(0,1),(0,2),(1,2)]
        self._moves = moves
            
    def get_move(self: 'MoveSequence', i: int):
        # Exception if not (0 <= i < self.length)
        return self._moves[i]
        
    def add_move(self: 'MoveSequence', src_stool: int, dest_stool: int):
        self._moves.append((src_stool, dest_stool))
        
    def length(self: 'MoveSequence') -> int:
        return len(self._moves)
    
    def generate_TOAHModel(self: 'MoveSequence', number_of_stools: int, 
                           number_of_cheeses: int) -> 'TOAHModel':
        """
        An alternate constructor for a TOAHModel. Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model
        
    def __repr__(self: 'MoveSequence') -> str:
        return "MoveSequence(" + repr(self._moves) + ")"


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
