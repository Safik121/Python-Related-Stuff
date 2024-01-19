import random

def find_treasure(width, steps):
    board = [[0] * width for _ in range(width)]
    treasure_location = (random.randint(0, width - 1), random.randint(0, width - 1))
    board[treasure_location[0]][treasure_location[1]] = 1

    current_position = (random.randint(0, width - 1), random.randint(0, width - 1))
    total_steps = 0

    for _ in range(steps):
        total_steps += 1
        move = random.choice(["N", "S", "E", "W"])
        if move == "N" and current_position[0] > 0:
            current_position = (current_position[0] - 1, current_position[1])
        elif move == "S" and current_position[0] < width - 1:
            current_position = (current_position[0] + 1, current_position[1])
        elif move == "E" and current_position[1] < width - 1:
            current_position = (current_position[0], current_position[1] + 1)
        elif move == "W" and current_position[1] > 0:
            current_position = (current_position[0], current_position[1] - 1)

        if current_position == treasure_location:
            return total_steps

    return None

def treasure_analysis(width, steps, count):
    treasure_count = 0
    total_steps_taken = 0

    for _ in range(count):
        result = find_treasure(width, steps)
        if result is not None:
            treasure_count += 1
            total_steps_taken += result

    if treasure_count > 0:
        success_percentage = (treasure_count / count) * 100
        average_steps = total_steps_taken / treasure_count
        print(f"Success Percentage: {success_percentage}%")
        print(f"Average Steps Taken to Find Treasure: {average_steps}")
    else:
        print("Bez Pokladu.")

treasure_analysis(10, 100, 100)
