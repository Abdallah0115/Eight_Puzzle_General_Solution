#----------------------imported lip----------------------------
import copy
from heuristic import mdh,mis_h

# #---------------------node of each state----------------------

class puzzel_node: # ********************* make a node of puzzel ******************

    state = [[],[],[]] # ***************** state of each node *********************

    act = ""

    out = False

    prev_st=""

    def __init__(self,st,prev_ac,prev_st) : #************* define state of this  node and position of blanck tile********************

        self.state = copy.copy(st) # ********** make a shallow copy of original list *************

        self.act = prev_ac

        self.prev_st = prev_st


#*********************** finds  tile position *****************

    def tile_now(self):

        blank = []

        for i in [0,1,2] :

            for j in [0,1,2] :

                if (self.state[i][j] == "b"):

                    blank.append(i) ; blank.append(j)

        return blank

    #***********************finds all possible actions ********************

    def Actions (self): 

        blank = self.tile_now()

        temp = []

        if(blank[0] != 0 and self.act != "b"):

            temp.append("t")

        if(blank[0] != 2 and self.act != "t"):

            temp.append("b")

        if(blank[1] != 0  and self.act != "r"):

            temp.append("l")

        if(blank[1] != 2 and self.act != "l" ):

            temp.append("r")

        return temp
    

    # ************************** returns the state of this node *********************

    def state_r (self): 

        return self.state

    #**************** returns result node of specefic action **************

    def results(self,action):  

        blank = self.tile_now()

        i1 = blank[0]

        j1 =blank[1]

        act = ""

        stat1 = copy.deepcopy(self.state)

        if(action == "t"):

            temp = stat1[i1][j1]

            stat1[i1][j1]=stat1[i1 - 1][j1] # top movement of tile 

            stat1[i1 - 1 ][j1] = temp

            act = "t"

        elif(action == "b"):

            temp = stat1[i1][j1]

            stat1[i1][j1]=stat1[i1 + 1][j1] # bottom movement of tile 

            stat1[i1 + 1 ][j1] = temp

            act = "b"

        elif(action == "l"):

            temp = stat1[i1][j1]

            stat1[i1][j1] = stat1[i1 ][j1 - 1] # left movement of tile 

            stat1[ i1 ][j1 - 1] = temp

            act = "l"

        elif(action == "r"):

            temp = stat1[i1][j1]

            stat1[i1][j1]=stat1[i1 ][j1 + 1] # right movement of tile 

            stat1[i1 ][j1 + 1] = temp

            act = "r"

        else :

            return None

        return puzzel_node(stat1,act,self)

    #**************** returns heuristc value of specefic node **************

    def hs(self,goal,choice):

        match choice:

            case 1:

                return mis_h(self.state_r(),goal)

            case 2:

                return mdh(self.state_r(),goal)

            case _:

                return mis_h(self.state_r(),goal)

    def out(self):

        return self














