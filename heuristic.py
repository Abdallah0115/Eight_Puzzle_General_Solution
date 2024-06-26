#--------search for the position of specific element----------------

def search(state, target):

    for i in range(3):

        for j in range(3):

            if state[i][j] == target:

                return [i, j]

#-----returns the mis placed heuristic value-------

def mis_h(current_state, goal_state):

    misplaced_count = 0

    for i in range(3):

        for j in range(3):

            if current_state[i][j] != goal_state[i][j] and current_state[i][j] != 'b':

                misplaced_count += 1

    return misplaced_count

#------return the manhaten distance heuristic valu-------

def mdh(current_state, goal_state):

    total_distance = 0

    for i in range(3):

        for j in range(3):

            if current_state[i][j] != goal_state[i][j] and current_state[i][j] != 'b':

                target = search(goal_state, current_state[i][j])

                total_distance += abs(i - target[0]) + abs(j - target[1])

    return total_distance