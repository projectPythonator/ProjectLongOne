"""this is the main module for c code"""
import codecs
import re
import time

import cBasicFunctionsBox
import cBasicCommentChecksv

def cReadIn():
    """this portion is going to be reading in the code from a file
    it also will be checking for certain chars that may show up
    as unicode"""

	with codecs.open('myinputpuy.txt') as f: # inside of open you can put any file name with txt you want to use to test it
		cCode = [line.decode('utf-8').strip() for line in f.readlines()]
	myLength = len(cCode)
	for index in xrange(myLength):
		cCode[index] = re.sub(u"(\u2018|\u2019)", "'", cCode[index])
    return cCode

def cMain():
    start_time = time.time()
    cCode = cReadIn()
    """these are the spot for tuples that contain the strings like int char and what not
    it also will contain bool variables that are used in main for now"""
    theType = ('int ','char ','string ','float ')
    simpleFunctionTypes = ('int ','char ','string ','float ','void ')
    isBlockBodyC = False # used to see if we are still inside a block body
    lineNum = 0
    rStack = 0
	"""this is the portion for all the lists that store lines in different sorted manners"""
    cForList = []
    cIfList = []
    cColList = []
    cWhileList = []
    cSimpleTypesList = []
    cLineCommentList = []
    cBlkCommentList = []
    cFunctionHeaderList = []
    clibraryList = []
    cBlockedCodeStack = []
    cBlocksLines = []
    cBlockedFinal = []
    cStructList = []
    #re.compile(r'/*.+?*/', re.MULTILINE)
    """this is one of the main loops that sort each line into seperat lists"""
    for i in cCode:
        lineNum += 1
        #this section is to check for brackets
        if cBasicFunctionsBox.cBlockBracketOpen(i):
            cBlockedCodeStack.append([lineNum,i])
            cBlocksLines.append([lineNum,0])
        if cBasicFunctionsBox.cBlockBracketClose(i) and False == isBlockBodyC:
            myVar = cBlockedCodeStack.pop()
            cBlockedFinal.append(cBlocksLines.pop())
            cBlockedFinal[rStack][1] = lineNum
            rStack += 1
        #this section is for common line occurrences
        if cBasicFunctionsBox.cForCheck(i) and False == isBlockBodyC:
            cForList.append([lineNum,i])
        elif cBasicFunctionsBox.cIfCheck(i) and False == isBlockBodyC:
            cIfList.append([lineNum,i])
        elif cBasicFunctionsBox.cWhileCheck(i) and False == isBlockBodyC:
            cWhileList.append([lineNum,i])
        elif cBasicFunctionsBox.cFunctionHeaderCheck(i,simpleFunctionTypes) and False == isBlockBodyC:
            cFunctionHeaderList.append([lineNum,i])
        elif cBasicFunctionsBox.cDeclarSimpleCheck(theType,i) and False == isBlockBodyC:
            cSimpleTypesList.append([lineNum,i])
        elif cBasicFunctionsBox.cColsCheck(i) and False == isBlockBodyC:
            cColList.append([lineNum,i])
        elif cBasicFunctionsBox.cStructChecker(i) and False == isBlockBodyC:
            cStructList.append([lineNum,i])
        elif cBasicFunctionsBox.cLibraryIncludes(i) and False == isBlockBodyC:
            clibraryList.append([lineNum,i])
        #comment portion
        if cBasicCommentChecks.cInLineCommentCheck(i):
            cLineCommentList.append([lineNum,i])
        elif cBasicCommentChecks.cBlkCommentStartCheck(i) and cBasicCommentChecks.cBlkCommentEndCheck(i):
            cBlkCommentList.append([lineNum,i])
        elif cBasicCommentChecks.cBlkCommentStartCheck(i):
            isBlockBodyC = True
            cBlkCommentList.append([lineNum,i[i.index('/*'):]])
        elif  cBasicCommentChecks.cBlkCommentEndCheck(i):
            cBlkCommentList.append([lineNum,i])
            isBlockBodyC = False
        elif isBlockBodyC:
            cBlkCommentList.append([lineNum,i])
    #this section is to show how the code was split up
    print
    print '##############################for loops################################'
    print
    for i in cForList:
        print i
    print
    print '############################normal lines###############################'
    print
    for i in cColList:
        print i
    print
    print '############################if statments###############################'
    print
    for i in cIfList:
        print i
    print
    print '#############################while loops###############################'
    print
    for i in cWhileList:
        print i
    print
    print '#############################simple type decs##########################'
    print
    for i in cSimpleTypesList:
        print i
    print
    print '###############################line comments###########################'
    print
    for i in cLineCommentList:
        print i
    print
    print '###############################Block Comments##########################'
    print
    for i in cBlkCommentList:
        print i
    print
    print '############################Function Headers###########################'
    print
    for i in cFunctionHeaderList:
        print i
    print
    print '############################The Libraries##############################'
    print
    for i in clibraryList:
        print i
    print
    print '##############################My Structs##############################'
    print
    for i in cStructList:
        print i
    print
    print '##############################My Breackets##############################'
    print
    cBlockedFinal.sort()
    for i in cBlockedFinal:
        print i
    print 'the code is ' + str(myLength) + ' long'
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    #call testing file for this script
