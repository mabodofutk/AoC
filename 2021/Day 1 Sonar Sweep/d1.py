

def get_input(filepath):
    """Get data from input file.
    """
    with open(filepath, 'r') as f:
        payload = [int(line.rstrip()) for line in f.readlines()]
    return payload


def count_increases(data: list) -> int:
    """Count the number of times a depth measurement increases.

    Args:
        data: list of measurement depth data

    Returns:
        Number of times a depth measurement increases.
    """
    res = 0
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            res += 1
    return res


def count_increases_of_sliding_window(data, window_size):
    """Count the number of times a depth measurement increases within a sliding window sum.

    Args:
        data: list of measurement depth data
        window_size: int, measurements within a window

    Returns:
        Number of times a depth measurement increases.
    """
    res = 0
    prev_window = sum(data[:window_size])
    for i in range(len(data)-window_size+1):
        curr_window = sum(data[i:i+window_size])
        if curr_window > prev_window:
            res += 1
        prev_window = curr_window
    return res


def main():
    data = get_input('input.txt')
    # print(data)
    total_increases = count_increases(data)
    print(total_increases)
    total_increases_of_sliding_window = count_increases_of_sliding_window(
        data, 3)
    print(total_increases_of_sliding_window)


if __name__ == '__main__':
    main()
