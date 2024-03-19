# Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed
# by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
# The operation will either be S (split) or C (combine)
# M indicates method, C indicates class, and V indicates variable
# In the case of a split operation, the words will be a camel case method,
# class or variable name that you need to split into a space-delimited list
# of words starting with a lowercase letter.
# In the case of a combine operation, the words will be a space-delimited
# list of words starting with lowercase letters that you need to combine
# into the appropriate camel case String. Methods should end with an empty
# set of parentheses to differentiate them from variable names.

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re


inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]

for line in inputData:
    split_input = line.split(";")

    if split_input[0] == "C":

        if split_input[1] == "C":

            split_out = split_input[2].split(" ")

            bigletter = " ".join(split_out[0:len(split_out)])

            bigletter = bigletter.title()

            result = bigletter.replace(" ", "")

            print(result)

        elif split_input[1] == "V":

            split_out = split_input[2].split(" ")

            bigletter = " ".join(split_out[1:len(split_out)])

            bigletter = bigletter.title()

            result = str(split_out[0]) + bigletter.replace(" ", "")

            print(result)


        elif split_input[1] == "M":

            split_out = split_input[2].split(" ")

            bigletter = " ".join(split_out[1:len(split_out)])

            bigletter = bigletter.title()

            result = str(split_out[0]) + bigletter.replace(" ", "") + "()"
            print(result)


    elif split_input[0] == "S":

        if split_input[1] == "C":
            words = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', split_input[2])

            result = " ".join(words)

            print(result.lower())

        if split_input[1] == "V":
            words = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', split_input[2])

            second_part = " ".join(words)

            first_word = str(split_input[2])[:-len(second_part.replace(" ", ""))]

            result = first_word + " " + second_part

            print(result.lower())

        if split_input[1] == "M":
            split_input[2] = str(split_input[2])[:-2]

            words = re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', split_input[2])

            second_part = " ".join(words)

            first_word = str(split_input[2])[:-len(second_part.replace(" ", ""))]

            result = first_word + " " + second_part

            print(result.lower())
