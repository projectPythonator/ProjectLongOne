"""this Module checks c code for comments"""
def cInLineCommentCheck(myLine):
    """cInLineCommentCheck(myLine)
    this is a function to check c Code
    this function will be checking c syntax code line for existence of a line comment
    pre myLine is a line of c code
    returns true if the code contains a line comment,false otherwise"""
    comment = '//'
    if comment in myLine:
        return True
    else:
        return False
def cBlkCommentStartCheck(myLine):
    """ cBlkCommentStartCheck(myLine):
    this is a function to check c Code
    this function will be checking c syntax code line for existence of a openning block comment symbol
    pre myLine is a line of code 
    returns true if '/*' is in the line myLine false otherwise"""
    comment = '/*'
    if comment in myLine:
        return True
    else:
        return False
def cBlkCommentEndCheck(myLine):
    """cBlkCommentEndCheck(myLine)
    this is a function to check c Code
    this function will be checking c syntax code line for existence of a closing block comment symbol
    pre myLine is a line of code
    returns true if '*/' is in the line myLine false otherwise"""
    comment = '*/'
    if comment in myLine:
        return True
    else:
        return False
