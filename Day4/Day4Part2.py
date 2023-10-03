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
    file_name = 'Day4Input.txt'
    day4_input = input_converter(file_name)
    results = entire_range_counter(day4_input)
    print(results)



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
    a = 0
    for i in input_file:
        if (int(i[0]) <= int(i[2]) <= int(i[1])) or\
                (int(i[2]) <= int(i[0]) <= int(i[3])) or \
                (int(i[0]) <= int(i[3]) <= int(i[1]))or \
                (int(i[2]) <= int(i[1]) <= int(i[3])):
            a += 1
    return a

if __name__ == '__main__':
    main()