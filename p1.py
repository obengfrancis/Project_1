
""" 
As a Hokie, I, <FRANCIS OBENG> ,  will conduct myself with honor and integrity at all times.  
I will not lie, cheat, or steal, nor will I accept the actions of those who do.”

"""
#############################################################################
################ DO NOT MODIFY THIS CODE ####################################
#############################################################################
import argparse
from autograder import *


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='A Python application to evaluate and translate postfix expressions', allow_abbrev=True)
    parser.add_argument('-i', '--input_file', type=str,
                        help='name of input file containing postfix expressions separated by newline')
    parser.add_argument('-o', '--output_file', type=str, nargs='?',
                        help='name of the output file to save the output')
    parser.add_argument('-m', '--mode', type=str,
                        help='mode of the script--Evaluator, Translator, or Tester', choices=['eval', 's2s', 'test'], required=True)
    args = parser.parse_args()
    return args


def main():
    output_lines = []
    try:
        with open(args.input_file) as file:
            lines = file.readlines()
            if args.mode == 'eval':
                output_lines = map(lambda x: evaluate(x).strip(), lines)

            else:
                output_lines = map(lambda x: postToInfix(x).strip(), lines)
            with open(args.output_file, 'w') as f:
                f.write('\n'.join(output_lines))
    except FileNotFoundError:
        msg = "ERROR: " + args.input_file + " does not exist."
        print(msg)
#############################################################################
################ Write your code below this line ############################
#############################################################################

""" 
Task 1 implementation goes here. Feel free to add more functions or classes.
"""

def evaluate(postfix_equation_string):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    print(f"Evaluating: {postfix_equation_string}")  # Monitoring the postfix_equation_string.

    for token in postfix_equation_string.split():
        if token.isdigit():  # This check if the token is a number
            stack.append(int(token))  # Convert the string to an integer and push it onto the stack
        elif token in operators:  # This check if token is an operator
            if len(stack) < 2:
                return "ERROR: Too few operands"
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            if token == '+':
                result = operand_1 + operand_2
            elif token == '-':
                result = operand_1 - operand_2
            elif token == '*':
                result = operand_1 * operand_2
            elif token == '/':
                if operand_2 == 0:
                    return "ERROR: Division by zero"
                result = operand_1 / operand_2
            stack.append(result)
    
    if len(stack) != 1:
        return "ERROR: Too many literals"
    
    return str(stack[0])

""" 
Task 2 implementation goes here. Feel free to add more functions or classes.
"""
def postToInfix(postfix_equation_string):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for token in postfix_equation_string.split():
        if token.isdigit():  #This check if the token is a number, push it onto the stack
            stack.append(token)
        elif token in operators:  # This check if the token is an operator
            if len(stack) < 2:
                return "ERROR: Too few operands"
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            # Combinning the two operands with the operator in infix form
            result = f"({operand_1} {token} {operand_2})"
            stack.append(result)
    
    if len(stack) != 1:
        return "ERROR: Too many literals"
    
    return stack[0]

#############################################################################
################ Write your code above this line ############################
#############################################################################
if __name__ == '__main__':
    args = parse_arguments()
    if args.mode == "test":
        test()
    else:
        main()
