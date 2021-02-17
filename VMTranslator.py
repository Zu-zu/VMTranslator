#!/usr/bin/env python3
import os
import argparse


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
    else:
        print("invalid input")

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
    elif arga == "temp":
        arg1 = "TEMP"
    elif arga =="pointer":
        arg1 = "POINT"
    elif arga =="static":
        arg1 ="STATIC"
    else:
        print("invalid arg1")
    return arg1, arg2

def writePushPop(command,segment,index,line,outputfile):
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

def writeArithmetic(segment,line,count,outputfile):
    if segment == "ADD":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM=M-1\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=M+D\n")
        f.close()
    elif segment =="SUB":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM=M-1\n")
        f.write("D=M\n")
        f.write("A=A-1\n")
        f.write("M=M-D\n")
        f.close()
    elif segment =="NEG":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("A=A-1\n")
        f.write("M=-M\n")
        f.close()
    elif segment =="EQ":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM = M-1\n")
        f.write("D = M\n")
        f.write("A = A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M-D;JEQ\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    elif segment == "LT":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM = M-1\n")
        f.write("D = M\n")
        f.write("A = A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M-D;JGT\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    elif segment == "GT":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM = M-1\n")
        f.write("D = M\n")
        f.write("A = A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M-D;JLT\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    elif segment == "AND":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM = M-1\n")
        f.write("D = M\n")
        f.write("A = A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M&D;JNE\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    elif segment == "OR":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("AM = M-1\n")
        f.write("D = M\n")
        f.write("A = A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M|D;JNE\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    elif segment == "NOT":
        f=open(outputfile,'a')
        f.write("//"+line)
        f.write("@SP\n")
        f.write("A=A-1\n")
        f.write("@ifTrue"+count+"\n")
        f.write("M;JEQS\n")
        f.write("@ifFalse"+count+"\n")
        f.wirte("0;JMP\n")
        f.write("(ifTrue"+count+")\n")
        f.wrtie("M=-1\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(ifFalse"+count+")\n")
        f.write("M=0\n")
        f.write("@Back"+count+"\n")
        f.write("0;JMP\n")
        f.write("(@Back"+count+")\n")
        f.close()
    else:
        print("command not available")


def Main():
    #prompt for the file name/location
    parser = argparse.ArgumentParser(description="Enter path or directory")
    parser.add_argument('filename',action = "store")
    parser.add_argument('-o','--outfile',action = "store",default = None,dest = 'outname')
    args = parser.parse_args()
    inputfile = args.filename
    outputfile = args.outname
    root,ext = os.path.splitext(inputfile)
    outputfile = root+".asm"
    linecount =0
    count =0
    with open(inputfile) as f:
        lines = f.readlines()
        for line in lines:
            count += 1
            linecount +=1
            print("line "+str(linecount))
            if line.startswith('//'):
                continue
            else:
                line.strip('\n')
                type = commandType(line)
                if type == "C_ARITHMETIC":
                    argument1 = whatArithmetic(line)
                    newlines = writeArithmetic(argument1,line,count,outputfile)
                elif type == "C_PUSH":
                    argument1, argument2 = getArguments(line)
                    newlines= writePushPop("PUSH",argument1,argument2,line,outputfile)
                elif type == "C_POP":
                    argument1, argument2 = getArguments(line)
                    newlines = writePushPop("POP",argument1,argument2,line,outputfile)
                else:
                    print("invalid type")




#Main("BasicTest.vm")
#Main("StaticTest.vm")
#Main("StackTest.vm")
#Main("SimpleAdd.vm")
#Main("PointerTest.vm")
Main()
