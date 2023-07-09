input_req = {'text': 3}

import argparse

# Create an argument parser
parser = argparse.ArgumentParser(description='Perform addition of two numbers.')

# Add command-line arguments
parser.add_argument('arg1', type=int, help='First number')
parser.add_argument('arg2', type=int, help='Second number')
parser.add_argument('arg3', type=int, help='Third number')

# Parse the command-line arguments
args = parser.parse_args()

input1 = args.arg1
input2 = args.arg2
input3 = args.arg3
# print(input1, input2, input3)
# print(type(input1))
# inputList = [input1, input2, input3]
# print('lst: ', inputList)
# flist = sorted(inputList)
# print('sorted list: ', flist)



def greaterNo(input1, input2, input3):
    inputList = [input1, input2, input3]
    flist = sorted(inputList)
    # print(flist[-1])
    return f'Greater number between {input1}, {input2} and {input3} is {flist[-1]}'

print(greaterNo(input1, input2, input3))


