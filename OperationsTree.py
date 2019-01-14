# -*- coding: utf-8 -*-
import sys

class operationsTree:

    def __init__(self):
        self.root = []
        self.actual = self.root
        self.previosToken = "none"

    def pushAdd(self):
        if (self.previosToken == "number") and (len (self.actual) == 0):
            self.actual.append("sum")
            self.actual.insert(0, self.tempNumber)
        elif (self.previosToken == "number") and (len (self.actual) > 0):
            self.actual.insert(0, self.tempNumber)
            temp = [self.actual, "sum"]
            self.root = self.actual = temp


        else:
            print ("Error: incorrect order of the operators")
            sys.exit(0)

        self.previosToken = "SumRest"


    def pushSub(self):
        if (self.previosToken == "number") and (len (self.actual) == 0):
            self.actual.append("sub")
            self.actual.insert(0, self.tempNumber)
        elif (self.previosToken == "number") and (len (self.actual) > 0):
            self.actual.insert(0, self.tempNumber)
            temp = [self.actual, "sub"]
            self.root = self.actual = temp


        else:
            print ("Error: incorrect order of the operators")
            sys.exit(0)

        self.previosToken = "SumRest"



    def pushNumber(self,number):
        self.tempNumber = number
        self.previosToken = "number"

    def pushMult(self):
        if (self.previosToken == "number") and (len (self.actual) == 0):
            self.actual.append("mul")
            self.actual.insert(0, self.tempNumber)
        elif (self.previosToken == "number") and (len (self.actual) > 0):
            if (self.actual[-1] == "sum") or (self.actual[-1] == "sub"):
                temp = [self.tempNumber, "mul"]
                self.actual.insert(0, temp)
                self.actual = temp
            elif(self.actual[-1] == "mul") or (self.actual[-1] == "div"):
                self.actual.insert(0, self.tempNumber)
                temp = [self.actual, "mul"]
                self.root = self.actual = temp



        else:
            print ("Error: incorrect order of the operators")
            sys.exit(0)

        self.previosToken = "MultDiv"

    def pushDiv(self):
        if (self.previosToken == "number") and (len (self.actual) == 0):
            self.actual.append("div")
            self.actual.insert(0, self.tempNumber)
        elif (self.previosToken == "number") and (len (self.actual) > 0):
            if (self.actual[-1] == "sum") or (self.actual[-1] == "sub"):
                temp = [self.tempNumber, "div"]
                self.actual.insert(0, temp)
                self.actual = temp
            elif(self.actual[-1] == "mul") or (self.actual[-1] == "div"):
                self.actual.insert(0, self.tempNumber)
                temp = [self.actual, "div"]
                self.root = self.actual = temp



        else:
            print ("Error: incorrect order of the operators")
            sys.exit(0)

        self.previosToken = "MultDiv"

    def calculate(self):
        if (self.previosToken == "number"):
            self.actual.insert(0, self.tempNumber)
            return self.__internalCalculate(self.root)
        else:
            print ("Error: an operand was missing at the end of the operation")
            sys.exit(0)

    def __internalCalculate(self,operation):
        ab = []

        i = 0
        while(i < 2):
            if (str(type(operation[i])) == "<type 'float'>") or (str(type(operation[i])) == "<type 'int'>"):
                ab.append(operation[i])
            elif(str(type(operation[i])) == "<type 'list'>"):
                ab.append(self.__internalCalculate(operation[i]))
            i = i + 1
        if(operation[2] == "sum"):
            return (ab[1] + ab[0])
        elif(operation[2] == "sub"):
            return (ab[1] - ab[0])
        elif(operation[2] == "mul"):
            return (ab[1] * ab[0])
        elif(operation[2] == "div"):
            return (ab[1] / ab[0])


    def imp(self):
        print (self.root)
