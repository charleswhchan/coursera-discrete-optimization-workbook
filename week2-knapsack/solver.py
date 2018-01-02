#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i-1, int(parts[0]), int(parts[1])))

    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    value = 0
    weight = 0
    taken = [0]*len(items)

    # for item in items:
    #     if weight + item.weight <= capacity:
    #         taken[item.index] = 1
    #         value += item.value
    #         weight += item.weight

    value = O(capacity, item_count, items, taken)
    # print(taken)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data

def O(k, j, items, taken):
    array_index = j - 1
    # print(j, "==>", taken)
    if (j == 0):
        return 0
    elif items[array_index].weight <= k:
        a = O(k, j-1, items, taken)
        b = items[array_index].value + O(k-items[array_index].weight, j-1, items, taken)

        if b > a:
            # print("b>a index {} a {} b {}".format(array_index, a, b))

            taken[array_index] = 1
            return b
        else:
            # print("a>b index {} a {} b {}".format(array_index, a, b))

            taken[array_index] = 0
            return a
    else:
        taken[array_index] = 0

        return O(k, j-1, items, taken)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

