#!/usr/bin/env python3
import os
inputfile = "samplecode.txt"
outputfile = "sampleasmcode.txt"

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
    command, arga, argb = line.split(' ')
    arg2 = int(argb)
    if arga =="constant":
        arg1 = "constant"
    elif arga == "local":
        arg1 = "LCL"
    elif arga == "argument":
        arg1 = "ARG"
    elif arga == "this":
        arg1 = "THIS"
    elif arga == "that":
        arg1 = "THAT"
    else:
        print("invalid arg1")

    return arg1, arg2

def writePushPop(command,segment,index,line):
    if command == "PUSH" and segment == "constant":
        f = open(outputfile,'a')
        f.write("//"+line)
        f.write("@"+str(index)+"\n")
        f.write("D=A"+"\n")
        f.write("@SP"+"\n")
        f.write("AM=M+1"+"\n")
        f.write("A=A-1"+"\n")
        f.write("M=D"+"\n")
        f.close()
    elif command =="PUSH":
        f = open(outputfile,'a')
        f.write("//"+line)
        f.write("@"+segment+"\n")
        f.write("D=M"+"\n")
        f.write("@"+str(index)+"\n")
        f.write("A=A+D"+"\n")
        f.write("D=M"+"\n")
        f.write("@SP"+"\n")
        f.write("AM=M+1"+"\n")
        f.write("A=A-1"+"\n")
        f.write("M=D"+"\n")
        f.close()
    elif command =="POP":
        f = open(outputfile,'a')
        f.write("//"+line)
        f.write("@"+segment+"\n")
        f.write("D=M"+"\n")
        f.write("@"+str(index)+"\n")
        f.write("D=D+A"+"\n")
        f.write("@R13"+"\n")
        f.write("M=D"+"\n")
        f.write("@SP"+"\n")
        f.write("AM=M-1"+"\n")
        f.write("D=M"+"\n")
        f.write("@R13"+"\n")
        f.write("A=M"+"\n")
        f.write("M=D"+"\n")
        f.close()
    else:
        print('Bad line bro')

#def writeArithmetic(segment,line):

def Main():
    #prompt for the file name/location
    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('//'):
                continue
            else:
                line.strip('\n')
                type = commandType(line)
                if type == "C_ARITHMETIC":
                    arg1 = whatArithmetic(line)
                    newlines = writeArithmetic(arg1,line)
                elif type == "C_PUSH":
                    arg1, arg2 = getArguments(line)
                    newlines= writePushPop("PUSH",arg1,arg2,line)
                elif type == "C_POP":
                    arg1, arg2 = getArguments(line)
                    newlines = writePushPop("POP",arg1,arg2,line)
                else:
                    print("invalid type")




Main()
