import heapq

class puzzle:
    def __init__(self):
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def input(self, state):
        for i in range(9):
            state.append(int(input(f"Enter element in position {i + 1}: ")))
        return state

    def hamming_distance(self, current_state, goal_state):
        distance = 0
        for i in range(9):
            if goal_state[i] != 0 and current_state[i] != goal_state[i]:
                distance += 1
        return distance

    def solve_puzzle(self, initial_state, goal_state):

        open_list = [(self.hamming_distance(initial_state, goal_state), 0, initial_state)]  # (estimated_total_cost, cuurent_cost, current_state
        closed_set = set()

        while open_list:
            total_distance, g, current_state = heapq.heappop(open_list)

            if current_state == goal_state:
                return g

            closed_set.add(tuple(current_state))

            zero_index = current_state.index(0)
            x, y = divmod(zero_index, 3)

            for dx, dy in self.moves:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < 3 and 0 <= new_y < 3:
                    new_index = (new_x * 3 + new_y)
                    new_state = current_state[:]
                    new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]

                    if tuple(new_state) not in closed_set:
                        heapq.heappush(open_list, (self.hamming_distance(new_state, goal_state), g + 1, new_state))

    def check(self, goal_state):
        puzzle = [num for num in goal_state if num != 0]
        inversions = 0

        for i in range(len(puzzle)):
            for j in range(i + 1, len(puzzle)):
                if puzzle[i] > puzzle[j]:
                    inversions += 1

        return inversions % 2

if __name__ == "__main__":
    initial_state = [1,3,4,0,5,8,7,2,6]
    goal_state = [1,2,3,4,5,6,7,8,0]

    p = puzzle()

    valid = p.check(goal_state)
    print(f"The no. of inversions are: {valid}")
    if valid == 1:
        print("Error, Puzzle Not Solvable")
        exit()

    steps = p.solve_puzzle(initial_state, goal_state)
    print(f"Minimum number of moves to solve the puzzle: {steps}")
