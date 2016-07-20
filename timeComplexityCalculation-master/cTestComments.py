from cBasicCommentChecks import *

def testing_comments():
    cFalseCommentLine = 'if hello there i am not a comment'
    cBOCTest1 = '/* hello there how is it going'
    cBOCTest2 = 'cout << "helloWorld" << endl;/* hello there how is it going'
    cBOCFail = '/ hey ther what is up *'
    cBCCTest1 = ' hello there how is it going*/'
    cBCCTest2 = ' hello there how is it going*/if(true)'
    cBCCFail = ' hey ther qhat is * up /'
    cLCTest1 = '// this is my line comment'
    cLCTest2 = 'while(true) //this runs forever'
    cLCTFail = '/i am not a comment'
    if cInLineCommentCheck(cLCTest1):
        print 'first test works as expected'
    else:
        print 'error the line comment checker does not work on test one'
    if cInLineCommentCheck(cLCTest2):
        print 'second test works as expected'
    else:
        print 'error the line comment checker does not work on test two'
    if cInLineCommentCheck(cLCTFail) == False:
        print 'the fail test works as expected'
    else:
        print 'error the line comment checker does not work on Fail test comment Line'
    if cInLineCommentCheck(cFalseCommentLine) == False:
        print 'general Fail test works as expected'
    else:
        print 'error the line comment checker does not work on General fail test'


    if cBlkCommentStartCheck(cBOCTest1):
        print 'first test works as expected for the block open comment checker'
    else:
        print 'error the block open comment checker does not work on test one of block comments open'
    if cBlkCommentStartCheck(cBOCTest2):
        print 'second test works as expected for the block open comment checker'
    else:
        print 'error the block open comment checker does not work on test two of block comments open'
    if cBlkCommentStartCheck(cBOCFail) == False:
        print 'fail test works as expected for the block open comment checker'
    else:
        print 'error the block open comment checker does not work on the fail test of block comments open'
    if cBlkCommentStartCheck(cFalseCommentLine) == False:
        print 'general fail test works as expected for the block open comment checker'
    else:
        print 'error the block open comment checker does not work on general Fail test of block comments open'
    if cBlkCommentEndCheck(cBCCTest1):
        print 'first close comment test works as expected for the block close comment checker'
    else:
        print 'error the block close comment checker does not work on test one close comment of block comments close'
    if cBlkCommentEndCheck(cBCCTest2):
        print 'second close test works as expected for the block close comment checker'
    else:
        print 'error the block close comment checker does not work on the second test of block comments close'
    if cBlkCommentEndCheck(cBCCFail)== False:
        print 'the fail close comment test works as expected for the block close comment checker'
    else:
        print 'error the block clsoe comment checker does not work on fail test of block comments close'
    if cBlkCommentEndCheck(cFalseCommentLine)== False:
        print 'the general fail comment test works as expected for the block close comment checker'
    else:
        print 'error the block clsoe comment checker does not work on general fail test of block comments close'

if __name__ == '__main__':
    testing_comments()
