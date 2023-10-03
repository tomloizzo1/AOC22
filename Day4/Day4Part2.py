'''
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''

def main():
    file_name = 'Day4Input.txt'                # Raw input file
    day4_input = input_converter(file_name)    # Input file cleaned up for iteration
    results = entire_range_counter(day4_input) # The answer to Day 4 part 2 Puzzle
    print(results)                             # Returns 895



def input_converter(file_name):
    """
    :param file_name: This is the Input to the Daily Puzzle
    :return: Returns the input as a single list of lists
    """
    final_input = []
    input_file = open(file_name, "r")
    input_string = input_file.read().splitlines()
    for i in input_string:
        list_maker = i.replace('-',',')
        list_maker = list_maker.split(",")
        final_input.append(list_maker)
    return final_input

def entire_range_counter(input_file):
    """
    :param input_file: The cleaned version of the input split into a list of lists
    :return:
    The count of how many lists have over lap in pairs [0,1] or [2,3] by checking if [2] or [3] falls between [0,1] or
    if [0] or [1] falls between [2,3]
    """
    overlap_counter = 0
    for i in input_file:
        if (int(i[0]) <= int(i[2]) <= int(i[1])) or\
                (int(i[2]) <= int(i[0]) <= int(i[3])) or \
                (int(i[0]) <= int(i[3]) <= int(i[1]))or \
                (int(i[2]) <= int(i[1]) <= int(i[3])):
            overlap_counter += 1
    return overlap_counter

if __name__ == '__main__':
    main()