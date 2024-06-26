#---------- importation ----------------

from  eight_puzzel import puzzel_node

#-------------------- work -------------------

class game:

    # return the lowest hueristic value node

    def the_lower(self,nodes_obj,goal,choice):

        nodes_obj=list(nodes_obj)

        less = nodes_obj[0].hs(goal,choice)

        for i in nodes_obj:

            match i.hs(goal,choice) < less:

                case True:

                    less =i.hs(goal,choice)

        return less

    #------------- append an node to the queue of nodes rejecting to found the same node towice------------

    def expands(self,nodes_obj,node):

        for i in node.Actions():

            nodes_obj.append(node.results(i))

        if(nodes_obj.__contains__(node)):

            nodes_obj.remove(node)

    #------------expand the lower node in the sequence---------------------

    def expand_lower(self,nodes_obj,less,goal,choice):

        for i in nodes_obj:

            match i.hs(goal,choice) == less:

                case True:

                    self.expands(self,nodes_obj,i)

    #------------displaying the sequance of solution------------------

    def dis (self,nodes_obj):

        for i in nodes_obj:

            print(i.state_r())

            if(nodes_obj.index(i)!=len(nodes_obj)-1):print('\n')

    #------------ return the sequance of solution--------------------

    def origin(self,node):

        nodes_obj = []

        while(node.act != 'in' ):

            nodes_obj.append(node)

            node = node.prev_st

        nodes_obj.reverse()

        return nodes_obj

    #------------- check if the goal is inside the sequence solution ------------------ 

    def pg(self,nodes_obj,goal,choice):

        for i in nodes_obj:

            match i.hs(goal,choice) == 0:

                case True:

                    return False

        return True

    # ------------- if it found the goal state return it ------------- 

    def ind_end(self,nodes_obj,goal,choice):

        for i in nodes_obj:

            match i.hs(goal,choice) == 0:

                case True:

                    return i

    #--------------displaying steps required to reach from initial state to the goal---------------- 

    def moves (self,nodes_obj):

        st = []

        for i in nodes_obj:

            if(i.act!='in'):

                if(i.act == "t"):

                    st.append(" UP ")

                elif(i.act == "b"):

                    st.append(" Down ")

                elif(i.act == "r"):

                    st.append( " Right ")

                elif(i.act == "l"):

                    st.append(" Left ")

        return st

    #---------------the function that return the solution of the game ---------------------

    def game_puzzle(self,initial,goalState,heurType):

        nodes_obj=[]

        out=""

        begin = initial

        goal = goalState

        choice = heurType

        root = puzzel_node(begin,"in","in")

        self.expands(self,nodes_obj,root)

        while (self.pg(self,nodes_obj,goal,choice)):

            self.expand_lower(self,nodes_obj,self.the_lower(self,nodes_obj,goal,choice),goal,choice)

        out = self.origin(self,self.ind_end(self,nodes_obj,goal,choice))

        return out