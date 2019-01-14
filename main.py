# -*- coding: utf-8 -*-


from plex import *
import sys


lexicon = []

digit = Range("09")
integerN = Rep1(digit)
NintegerN = Str("-") + integerN
floatN = Rep(digit) + Str(".") + Rep1(digit)
NfloatN = Str("-") + Rep(digit) + Str(".") + Rep1(digit)

lexicon.append((NintegerN, "Nint"))
lexicon.append((integerN, "int"))
lexicon.append((floatN, "flt"))
lexicon.append((NfloatN, "Nflt"))

lexicon.append((Str("+"), "sum"))
lexicon.append((Str("-"), "sub"))
lexicon.append((Str("/"), "div"))
lexicon.append((Str("*"), "mul"))

lexicon.append((Rep1(Any(" \t\n")), IGNORE))
lexicon.append((AnyBut(""), "Error, the token is not recognized"))

lexicon = Lexicon(lexicon)


from sys import argv

if len(argv) >= 2:
        filename = argv[1]
else:
        print "The file to be analyzed was not defined"
        sys.exit(0)
f = open(filename, "r")
scanner = Scanner(lexicon, f, filename)


from OperationsTree import operationsTree
opt = operationsTree()

while 1:
    token = scanner.read()
    pos = scanner.position()

    if (str(token[0]) == "int") or (str(token[0]) == "Nint"):
        opt.pushNumber(int(token[1]))
    if (str(token[0]) == "flt") or (str(token[0]) == "Nflt"):
        opt.pushNumber(float(token[1]))
    elif(str(token[0]) == "sum"):
        opt.pushAdd()
    elif(str(token[0]) == "sub"):
        opt.pushSub()
    elif(str(token[0]) == "div"):
        opt.pushDiv()
    elif(str(token[0]) == "mul"):
        opt.pushMult()
    elif token[0] is None:
        print ("╔═════════════════╦════════════════╗")
        print ("║" + "Result".center(17," ") + "║" +  str(opt.calculate()).center(16," ") + "║")
        print ("╚═════════════════╩════════════════╝")
        #opt.imp()
        break

