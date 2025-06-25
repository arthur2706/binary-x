#!/usr/bin/python

import sys
import argparse

def get_x_positions(input):
    positions = []
    for i in range(len(input)):
        if input[i] == 'X':
            positions.append(i)
    return positions

def i_on_xpositions_mask(i, xpositions):
    """
    The function takes a number 'i' and X's position list,
    for each bit in 'i' it will shift it to X position filling spaces with 0's.
    i.e.
    i = 0000111 and xpositions[0, 2, 4] it'll create output: 0010101

    """
    output = 0
    for xpos in xpositions:
        # for each bit in i, mask it to current X position
        output |= ((i << xpos) & (1 << xpos))
        i = i >> 1
    return output


def printCombinationsFast(input):
    """
    We create an input number template (mask) that has all original input numbers bits with 0's instead of X's.
    Algo generates each binary number from 0 to 2^X, and using bit manipulation shifts,
    inserts this number's bits into X positions in input number using input's template.

    O(X2^X) where X is the number of X's inside the input string.
    O(1) MEM
    """
    fmt = '0' + str(len(input)) + 'b'

    xpositions = get_x_positions(input[::-1])
    # 10X10X0 => 1001000
    #              ^  ^
    template = long(''.join(map(lambda ch: '0' if ch == 'X' else ch, input)), 2)

    # count number of X's
    numer_of_x = len(filter(lambda ch: ch == 'X', input))
    numbers_to_generate = 1 << numer_of_x # 2 ^ X

    i = 0
    while i<numbers_to_generate:
        number = template | i_on_xpositions_mask(i, xpositions)
        print( format(number, fmt))
        i += 1


def printCombinations(input):
    """
    Algo generates each binary number from 0 to 2^N, and using bit manipulation,
    and checks if bits at non-X positions are the same a in the input, if same print number.

    O(2^N) where N is the length of the input string.
    O(1) MEM
    """

    andMask = long(''.join(map(lambda ch: '0' if ch == 'X' else '1', input)), 2)
    xorMask = long(''.join(map(lambda ch: '0' if ch == 'X' else ch, input)), 2)
    bignumber = 1 << len(input) # 2 ^ len
    fmt = '0' + str(len(input)) + 'b'
    i=0
    while i<bignumber:
        if not (i & andMask) ^ xorMask:
            print (format(i, fmt))
        i+=1


def printCombinationsRecursive(input, index):
    """
    Algo runs recursively over the input string generating the next pair of binary string to generate for each X it encounters.

    O(2^X) where X is the length of the input string.
    O(2^X) MEM of call stack.
    """
    if len(input) == index:
        print ("".join(input))
        return

    for i in range(index, len(input)):
        if input[i] == 'X':
            cp = input[:]
            cp[i] = '0'
            printCombinationsRecursive(cp, i+1)
            cp = input[:]
            cp[i] = '1'
            printCombinationsRecursive(cp, i+1)
            return

    print ("".join(input))


def validate(input):
    return len(filter(lambda ch: ch != '0' and ch != '1' and ch != 'X', input)) == 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("i", type=str, help="input binary string pattern with X for replacement.")
    parser.add_argument("-f", action="store_true", help="run in fast mode.")
    parser.add_argument("-r", action="store_true", help="run in recursive mode.")
    args = parser.parse_args()

    try:
        if not validate(args.i):
            raise ValueError("Input string is not a valid binary pattern.")
        if args.f: # fast mode
            printCombinationsFast(args.i)
        elif args.r: # recursive mode
            printCombinationsRecursive(list(args.i), 0)
        else:
            printCombinations(args.i)
    except Exception as error:
            print( repr(error))
            print( "Usage: ./paxosx 0X111X000")


if __name__ == "__main__":
    main()