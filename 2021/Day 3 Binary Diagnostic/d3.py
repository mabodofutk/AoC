from math import gamma


def get_input(filepath):
    """Get data from input file.
    """
    with open(filepath, 'r') as f:
        payload = [line.rstrip() for line in f.readlines()]
    return payload


def get_gamma_and_epsilon(data):
    """Get gamma rating and epsilon rating bit from data.

    Args:
        data: list of strings

    Returns:
        (gamma,epsilon): tuple of strings
    """
    gamma = ''
    epsilon = ''
    size = len(data)
    bits = {k: 0 for k in range(len(data[0]))}
    for entry in data:
        for idx, c in enumerate(entry):
            bits[idx] += int(c)
    for k, v in bits.items():
        if v >= size/2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    return (gamma, epsilon)


def get_oxygen_and_co2(data):
    """Get oxygen generator rating and CO2 scrubber rating bit from data.

    Args:
        data: list of strings

    Returns:
        (oxygen,co2): tuple of strings
    """
    oxygen = ''
    co2 = ''
    size = len(data[0])
    data_oxygen = data[:]
    data_co2 = data[:]
    for i in range(size):
        ones_oxygen = sum([int(b[i]) for b in data_oxygen])
        ones_co2 = sum([int(b[i]) for b in data_co2])
        if len(data_oxygen) == 1:
            oxygen += data_oxygen[0][i]
        elif ones_oxygen >= len(data_oxygen)/2:
            oxygen += '1'
        else:
            oxygen += '0'
        if len(data_co2) == 1:
            co2 += data_co2[0][i]
        elif ones_co2 >= len(data_co2)/2:
            co2 += '0'
        else:
            co2 += '1'
        data_oxygen = [
            entry for entry in data_oxygen if entry[i] == oxygen[-1]]
        data_co2 = [entry for entry in data_co2 if entry[i] == co2[-1]]
    return (oxygen, co2)


def main():
    data = get_input('input.txt')
    # data = ['00100',
    #         '11110',
    #         '10110',
    #         '10111',
    #         '10101',
    #         '01111',
    #         '00111',
    #         '11100',
    #         '10000',
    #         '11001',
    #         '00010',
    #         '01010']
    # print(data[:5])
    gamma_bit, epsilon_bit = get_gamma_and_epsilon(data)
    gamma, epsilon = int(gamma_bit, base=2), int(epsilon_bit, base=2)
    print(gamma, epsilon, gamma*epsilon)
    oxygen_bit, co2_bit = get_oxygen_and_co2(data)
    # print(oxygen_bit,co2_bit)
    oxygen, co2 = int(oxygen_bit, base=2), int(co2_bit, base=2)
    print(oxygen, co2, oxygen*co2)


if __name__ == '__main__':
    main()
