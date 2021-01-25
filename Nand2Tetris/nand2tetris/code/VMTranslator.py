#!/usr/bin/env python3
import os

sample='''
push constant 10
pop local 0
push constant 21'''


def Main:
    #prompt for the file name/location
    vmfilelocation = input("Please input the path to file: ")
    filename, fileext = os.path.splitext(vmfilelocation)


    #create the asm file
    asmfilename = filename + '.asm'
    asmfile = open(asmfilename,'w')

    #initiate the loop
    with open(vmfilelocation,'r') as vmfile:
        line = vmfile.readline()
        while line:
            print("//",line)
            

    #What is the command type?

    #get arg1

    #get arg2

    #write the initial line as a comment in the new file

    #Is it a push/pop or arthmetic/logic?

    #For arthmetic, write the output code

    #For push/pop, write the output code

    #close the loop

Main()
