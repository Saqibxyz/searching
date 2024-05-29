from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_capacity):
    """
    Solves the Water Jug problem using BFS.

    Args:
    jug1_capacity (int): Capacity of the first jug.
    jug2_capacity (int): Capacity of the second jug.
    target_capacity (int): Target capacity to reach.

    Returns:
    A list of steps to reach the target capacity, or None if it's not possible.
    """
    queue = deque([(0, 0, [])])  # Initialize queue with initial state (0, 0, [])
    visited = set((0, 0))  # Keep track of visited states

    while queue:
        jug1, jug2, steps = queue.popleft()

        # If we've reached the target capacity, return the steps
        if jug1 == target_capacity or jug2 == target_capacity or jug1 + jug2 == target_capacity:
            return steps + [(jug1, jug2)]

        # Generate next states
        for next_state in [
            (jug1_capacity, jug2),  # Fill jug1
            (0, jug2),  # Empty jug1
            (jug1, jug2_capacity),  # Fill jug2
            (jug1, 0),  # Empty jug2
            (max(0, jug1 - (jug2_capacity - jug2)), min(jug2_capacity, jug1 + jug2)),  # Pour jug1 into jug2
            (min(jug1_capacity, jug1 + jug2), max(0, jug2 - (jug1_capacity - jug1))),  # Pour jug2 into jug1
        ]:
            if next_state not in visited:
                queue.append((*next_state, steps + [(jug1, jug2)]))
                visited.add(next_state)

    return None  # If no solution is found

# Example usage:
jug1_capacity = int(input("Enter jug 1 capacity"))
jug2_capacity = int(input("Enter jug 2 capacity"))
target_capacity =int(input("Target"))

solution = water_jug_problem(jug1_capacity, jug2_capacity, target_capacity)
if solution:
    print("Solution found:")
    print("(jug1,jug2)")
    for step in solution:
        print(f"({step[0]}, {step[1]})")
else:
    print("No solution found.")