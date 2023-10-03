'''
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''

def main():
    print('hello world')
    file_name = 'Day1Input.txt'
    day1_input = input_converter(file_name)
    final_list = sum_list_generator(day1_input)
    final_list.sort(reverse=True)
    top_three_total = top_three(final_list)
    print(top_three_total)

def input_converter(file_name):
    """
    :param file_name: This is the Input to the Daily Puzzle
    :return: Returns the input as a single string
    """
    input_file = open(file_name, "r")
    input_string = input_file.read().splitlines()
    return input_string

def sum_list_generator(list_input):
    maximum = 0
    final_list = []
    for i in list_input:
        if i == '':
            final_list.append(maximum)
            maximum = 0
        else:
            maximum += int(i)
    return final_list

def top_three(lists):
    total = 0
    for i in lists[0:3]:
        total += int(i)
    return total

if __name__ == '__main__':
    main()
