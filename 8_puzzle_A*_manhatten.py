import heapq

class puzzle:
    def __init__(self):
        self.moves = [(-1, 0),(1,0),(0,-1),(0,1)]

    def input(self, state, l):
        for i in range(l*l):
            state.append(int(input(f"Enter element in position {i+1}: ")))
        return state
    
    def manhattan_distance(self, current_state, goal_state, l):
        distance = 0;
        for i in range(l*l):
            if goal_state[i] != 0:  # Skip the empty space
                j = current_state.index(goal_state[i])  # Find the index of the current element in current_state
                x1, y1 = divmod(i, l)
                x2, y2 = divmod(j, l)
                distance += abs(x1 - x2) + abs(y1 - y2)

        return distance

    def solve_puzzle(self, initial_state, goal_state, l):

        open_list = [(self.manhattan_distance(initial_state, goal_state, l), 0, initial_state)] # (estimated_total_cost, cuurent_cost, current_state
        closed_set = set()
        parent_map = {}

        while open_list:
            random_variable, g, current_state = heapq.heappop(open_list)
            
            if current_state == goal_state:
                path = [current_state]
                while tuple(current_state) in parent_map: # Need to make everything immutable 
                    current_state = parent_map[tuple(current_state)]
                    path.append(current_state)

                path.reverse()
                return g, path

            closed_set.add(tuple(current_state))
            zero_index = current_state.index(0)
            x, y = divmod(zero_index, l)

            for dx, dy in self.moves:
                new_x, new_y = x + dx, y + dy 
                if 0 <= new_x < l and 0 <= new_y < l:
                    new_index = (new_x * l + new_y)
                    new_state = current_state[:]
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

                    if tuple(new_state) not in closed_set:
                        heapq.heappush(open_list, (self.manhattan_distance(new_state, goal_state, l), g + 1, new_state))
                        parent_map[tuple(new_state)] = current_state
        return -1

    def check_inversions(self, state):
        inversions = 0
        state_flat = [num for num in state if num != 0] # Matrix in arry without 0

        for i in range(len(state_flat)):
            for j in range(i+1, len(state_flat)):
                if state_flat[i] > state_flat[j]:
                    inversions += 1
        
        print("The number of inversions are = ", inversions)
        return inversions

    def is_solvable(self, initial_state, goal_state, l): # Applies 8 puzzle validity rules
        if(p.check_inversions(initial_state) % 2 == p.check_inversions(goal_state) % 2):    
            n = int(len(initial_state) / l)
#            print("The value of n = ", n)
            
            if(n % 2 == 0):
                zero_index = initial_state.index(0)
                if(n % 2 == zero_index % 2):
                    return True
                
            else:
                if(p.check_inversions(initial_state) % 2 == 0 and p.check_inversions(goal_state) % 2 == 0):
                    return True
                
        
if __name__ == "__main__":
#    initial_state = []
#    goal_state = []

    initial_state = [1,3,4,0,5,7,8,2,6] # Not Working
    goal_state = [1,2,3,4,5,6,7,8,0]

#    initial_state = [1,3,4,5,7,8,6,0,2] # Working
#    goal_state = [1,2,3,4,5,6,7,8,0]

    p = puzzle()

    l = int(input("Enter the order of the matrices: ")) # Size of Matrix
#    print("Enter Initial State: ")
#    p.input(initial_state, l)
#    print("Initial State: ", initial_state)
    
#    print("Enter Goal State: ")
#    p.input(goal_state, l)
#    print("Enter Goal State: ", goal_state)

    test = p.is_solvable(initial_state, goal_state, l) # Check if puzzle can be solved 
    if test == False:
        print("Error, Not Solvable")
        exit()

    steps, path = p.solve_puzzle(initial_state, goal_state, l) # A* implementation
    print(f"Minimum number of moves to solve the puzzle: {steps}")

    if steps == -1:
        print("No solution found.")
    else:
        for step, state in enumerate(path):
            print(f"Step {step + 1}:")
            for i in range(l):
                print(state[i * l:i * l + l])
            print()