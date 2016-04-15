#############################################################################################################################
'''								FUNCTIONS THAT CHECK C CODE FOR COMMENTS       											  '''
#############################################################################################################################
""" 
	cInLineCommentCheck(myLine)
	this is a function to check c Code
	this function will be checking c syntax code line for existence of a line comment
    
    pre myLine is a line of c code
    
    returns true if the code contains a line comment,false otherwise
"""
def cInLineCommentCheck(myLine):
    comment = '//'
    if comment in myLine:
        return True
    else:
        return False

""" 
	cBlkCommentStartCheck(myLine):
	this is a function to check c Code
	this function will be checking c syntax code line for existence of a openning block comment symbol
    
    pre myLine is a line of code
    
    returns true if '/*' is in the line myLine false otherwise
"""
def cBlkCommentStartCheck(myLine):
    comment = '/*'
    if comment in myLine:
        return True
    else:
        return False

""" 
	cBlkCommentEndCheck(myLine)
	this is a function to check c Code
	this function will be checking c syntax code line for existence of a closing block comment symbol
    
    pre myLine is a line of code
    
    returns true if '*/' is in the line myLine false otherwise
"""
def cBlkCommentEndCheck(myLine):
    comment = '*/'
    if comment in myLine:
        return True
    else:
        return False