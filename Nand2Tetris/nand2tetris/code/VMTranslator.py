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


def Main():
    #prompt for the file name/location
    with open('samplecode.txt') as f:
        lines = f.readlines()
        for line in lines:
            line.strip('\n')
            type = commandType(line)
            print(type)



    #create the asm file


    #initiate the loop


    #What is the command type?

    #get arg1

    #get arg2

    #write the initial line as a comment in the new file

    #Is it a push/pop or arthmetic/logic?

    #For arthmetic, write the output code

    #For push/pop, write the output code

    #close the loop

Main()
