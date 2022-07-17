def get_input(filepath):
    """Get data from input file.
    """
    with open(filepath, 'r') as f:
        payload = [(line.rstrip().split()[0], int(line.rstrip().split()[1]))
                   for line in f.readlines()]
    return payload


def move(start, action):
    """Move according to the action.

    Args:
        start: tuple, (horizontal,depth), starting point
        action: tuple, (command,unit)

    Returns:
        position: tuple, (horizontal,depth)
    """
    command, unit = action
    horizontal, depth = start
    if command == 'forward':
        horizontal += unit
    elif command == 'down':
        depth += unit
    elif command == 'up':
        depth -= unit
    return horizontal, depth


def move_p2(start, action):
    """Move according to the action.

    Args:
        start: tuple, (horizontal,depth,aim), starting point
        action: tuple, (command,unit)

    Returns:
        position: tuple, (horizontal,depth,aim)
    """
    command, unit = action
    horizontal, depth, aim = start
    if command == 'forward':
        horizontal += unit
        depth += aim*unit
    elif command == 'down':
        aim += unit
    elif command == 'up':
        aim -= unit
    return horizontal, depth, aim


def batch_move(start, plan, move_method):
    """Move according to the plan (list of actions).

    Args:
        start: tuple, starting point
        plan: list of tuples, (command,unit)
        move_method: function, takes in start and (command,unit), return position after one move

    Returns:
        position: tuple
    """
    for a in plan:
        start = move_method(start, a)
    return start


def main():
    data = get_input('input.txt')
    # print(data[:5])
    start = (0, 0)
    pos = batch_move(start, data, move)
    print(pos, pos[0]*pos[1])
    start = (0, 0, 0)
    pos_p2 = batch_move(start, data, move_p2)
    print(pos_p2, pos_p2[0]*pos_p2[1])


if __name__ == '__main__':
    main()
