#!/usr/bin/env python3
import os

sample='''
push constant 10
pop local 0
push constant 21'''

def commandType(line):
    if line.startswith('push'):
        return "C_PUSH"
    elif line.startswith('pop'):
        return "C_POP"
    else:
        return "C_ARITHMETIC"

def whatArithmetic(line):
    if line.startswith('add'):
        return "ADD"
    elif line.startswith('sub'):
        return "SUB"
    elif line.startswith('neg'):
        return "NEG"
    elif line.startswith('eq'):
        return "EQ"
    elif line.startswith('lt'):
        return "LT"
    elif line.startswith('gt'):
        return "GT"
    elif line.startswith('and'):
        return "AND"
    elif line.startswith('or'):
        return "OR"
    elif line.startswith('not'):
        return "NOT"

def getArguments(line):
    command, arg1, argg = line.split(' ')
    arg2 = int(argg)
    return arg1, arg2


def Main():
    #prompt for the file name/location
    with open('samplecode.txt') as f:
        lines = f.readlines()
        for line in lines:
            line.strip('\n')
            type = commandType(line)
            if type == "C_ARITHMETIC":
                arth_type = whatArithmetic(line)
            if type == "C_PUSH" or type == "C_POP":
                arg1, arg2 = getArguments(line)
            



Main()
