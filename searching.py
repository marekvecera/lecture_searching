import os
import json
from math import floor

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as file:
        data = json.load(file)

    return data[field]


def linear_search(seq, target_num):
    output = {}
    pocet = 0
    indexes = []
    for idx, item in enumerate(seq):
        if item == target_num:
            pocet += 1
            indexes.append(idx)
    output['positions'] = indexes
    output['count'] = pocet

    return  output


def pattern_search(seq, target_pattern):
    output = []
    for i in range(len(seq) - len(target_pattern) + 1):
        if seq[i: i+len(target_pattern)] == target_pattern:
            output.append(i)
    return output


def binary_search(search_lst, target_num, offset_idx = 0):
    if not search_lst:
        return None
    split_idx = floor((len(search_lst) - 1)/2)
    act = search_lst[split_idx]
    if act == target_num:
        return split_idx + offset_idx
    else:
        if act > target_num:
            ret = binary_search(search_lst[:split_idx], target_num, offset_idx)
        else:
            ret = binary_search(search_lst[split_idx+1:], target_num, split_idx+1)
    return ret


def main():
    # sequential_data = read_data("sequential.json", "unordered_numbers")
    # hledani = linear_search(sequential_data, 9)
    # # print(hledani)
    #
    # dna_sequence = read_data("sequential.json", "dna_sequence")
    # hledani = pattern_search(dna_sequence, "ATA")
    # # print(hledani)

    ordered_nums = read_data("sequential.json", "ordered_numbers")
    hledani = binary_search(ordered_nums, 9)
    print(hledani)

if __name__ == '__main__':
    main()