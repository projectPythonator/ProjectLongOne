"""module for simple c function checking"""
#this section of functions will usually be in three sections because
#we need to make sure the string for is in the line as a forloop
#and not just inside of some kind of comment
#block comment case is if the line contains a block comment
#line comment case is if the line contains a line comment
#normal case if the line is just a line on its own
from cBasicCommentChecks import *

def cLineCommentIndexing(myLine,mSO):
    """ cLineCommentIndexing(myLine,mSO)
    this is a function to check c Code
    this function will be checking c code line for indexing
    pre myLine is a line of code
        mSO is a string to check for
    returns true if the string is before a comment false otherwise"""
    lnCom = '//'
    if myLine.index(mSO) < myLine.index(lnCom):
        return True
    return False

def cBlockCommentIndexing(myLine,mSO):
    """ cBlockCommentIndexing(myLine,mSO)
    this is a function to check c Code
    this function will be checking c code line for indexing
    pre myLine is a line of code
        mSO is a string to check for
    returns true if the string is before a comment false otherwise"""  
    bkCom = '/*'
    if myLine.index(mSO) < myLine.index(bkCom):
        return True
    return False

def cBlockCommentChecking(myLine,mSO):
    """ cBlockCommentchecking(myLine,mSO)
    this is a function to check c Code
    this function will be checking c code line for existence and indexing
    pre myLine is a line of code
        mSO is a string to check for
    returns true if the string is in myLine and before a comment false otherwise"""  
    blkCom = '/*'
    if all(a in myLine for a in mSO) and cBlockCommentIndexing(myLine,mSO[0]):
        return True
    return False

def cLineCommentChecking(myLine,mSO):
    """cLineCommentchecking(myLine,mSO)
    this is a function to check c Code
    this function will be checking c code line for existence and indexing
    pre myLine is a line of code
        mSO is a string to check for
    returns true if the string is in myLine and before a comment false otherwise"""  
    lnCom = '//'
    if all(a in myLine for a in mSO) and cLineCommentIndexing(myLine,mSO[0]):
        return True
    return False

def cForCheck(myLine):
    """ cForCheck(myLine)
    this is a function to check c Code
    this function will be checking c code line for for loop statements
    pre myLine is a line of code
    returns true if the line is a forloop statment false otherwise"""
    rStuff = ['for',';']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case 
    elif all(a in myLine for a in rStuff):
        return True
    else:
        return False

def cIfCheck(myLine):
    """ cIfCheck(myLine)
    this is a function to check c Code
    this function will be checking c code line for if statements
    pre myLine is a line of code
    returns true if the line is an if statment false otherwise"""
    rStuff = ['if','else']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case 
    elif any(a in myLine for a in rStuff):
        return True
    else:
        return False

def cColsCheck(myLine):
    """ cColsCheck(myLine)
    this is a function to check c Code
    this function will be checking c code line for existence of colons
    pre myLine is a line of code
    returns true if ';' is in the line myLine false otherwise"""
    rStuff = [';']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case 
    elif all(a in myLine for a in rStuff):
        return True
    else:
        return False

def cDeclarSimpleCheck(myType,myLine):
    """ cDeclarSimpleCheck(myType,myLine)
    this is a function to check c Code
    this function will be checking c code line to see if it is a simple type declaration of a primitive variable
    pre myLine is a line of code
        myType is a list containing strings of primitive variables
    returns true if the line is any of the variables that are primitive type decs , false otherwise"""
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        for a in myType:
            if a in myLine and cBlockCommentIndexing(myLine,a):
                return True
        else:
            return False
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        for a in myType:
            if a in myLine and cLineCommentIndexing(myLine,a):
                return True
        else:
            return False
    #this is the normal case 
    else:
        for a in myType:
            if a in myLine:
                return True
        else:
            return False
    return False

def cWhileCheck(myLine):
    """ cWhileCheck(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if it is a while loop statment
    pre myLine is a line of code
    returns true if the line is a while loop statment , false otherwise"""
    rStuff = ['while']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case 
    elif all(a in myLine for a in rStuff):
        return True
    else:
        return False

def cFunctionHeaderCheck(myLine,simpleFunctionTypes):
    """ cFunctionHeaderCheck(myLine,simpleFunctionTypes)
    this is a function to check c Code
    this function will be checking c code line to see if it is a function header
    pre myLine is a line of code
        simpleFunctionTypes is a list of strings containing common function return types
    returns true if the line is a function Header, false otherwise"""
    brackOpen = '('
    brackClose = ')'
    lefts = 0 
    rights = 0
    isFunction = False
    for i in myLine:
        if i == brackOpen:
            rights += 1
        elif i == brackClose:
            lefts += 1
    for i in simpleFunctionTypes:
        if i in myLine:
            isFunction = True
    if lefts+rights > 1 and isFunction == True:
    #this is the block comment case
        if cBlkCommentStartCheck(myLine):
            for a in simpleFunctionTypes:
                if a in myLine and myLine.index(a) < myLine.index(brackOpen) and cBlockCommentIndexing(myLine,a):
                    return True
            else:
                return False 
        elif cInLineCommentCheck(myLine):
            for a in simpleFunctionTypes:
                if a in myLine and myLine.index(a) < myLine.index(brackOpen) and cLineCommentIndexing(myLine,a):
                    return True
            else:
                return False
        else:
            for a in simpleFunctionTypes:
                if a in myLine:
                    if (myLine.index(a) < myLine.index(brackOpen)):
                        return True
            return False
    else:
        return False

def cBlockBracketOpen(myLine):
    """ cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an openiong bracket on the line
    pre myLine is a line of code
    returns true if the line is a an open bracket, false otherwise"""
    rStuff = ['{']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case
    elif rStuff[0] in myLine:
        return True
    else:
        return False

def cBlockBracketClose(myLine):
    """ cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an closing bracket on the line
    pre myLine is a line of code
    returns true if the line is a close bracket, false otherwise"""
    rStuff = ['}']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case
    elif rStuff[0] in myLine:
        return True
    else:
        return False

def cLibraryIncludes(myLine):
    """ cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an include statment on the line
    pre myLine is a line of code
    returns true if the line is a for libraries in the program, false otherwise"""
    rStuff = ['#include','<','>']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case
    elif all(a in myLine for a in rStuff):
        return True
    else:
        return False

def cStructChecker(myLine):
    """ cStructChecker(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an structs on the line
    pre myLine is a line of code
    returns true if the line is a for structs in the program, false otherwise"""
    rStuff = ['struct ']
    #this is the block comment case
    if cBlkCommentStartCheck(myLine):
        return cBlockCommentChecking(myLine,rStuff)
    #this is the line comment case
    elif cInLineCommentCheck(myLine):
        return cLineCommentChecking(myLine,rStuff)
    #this is the normal case
    elif all(a in myLine for a in rStuff):
        return True
    else:
        return False

if __name__ == '__main__':
	#call testing file for this script
