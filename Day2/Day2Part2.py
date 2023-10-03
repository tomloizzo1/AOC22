'''
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs
to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round
ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose
Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly
 according to your strategy guide?

'''

def main():
    file_name = 'Day2Input.txt'
    day2_input = input_converter(file_name)
    answer = score_calculator(day2_input)
    test(day2_input)
    print(answer)

def input_converter(file_name):
    """
    :param file_name: This is the Input to the Daily Puzzle
    :return: Returns the input as a single string
    """
    input_file = open(file_name, "r")
    input_string = input_file.read().splitlines()
    return input_string

def score_calculator(input_file):
    """A/X = ROCK, B/Y = PAPER C/Z = SCISSORcd..S"""
    score_dict = {"A X": 3, "B X": 1, "C X": 2, "A Y": 4, "B Y":  5, "C Y":  6, "A Z": 8, "B Z": 9, "C Z": 7, }
    sum = 0
    for i in input_file:
        sum += score_dict[i]
    return sum
if __name__ == '__main__':
    main()