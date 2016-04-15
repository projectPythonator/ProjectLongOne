#############################################################################################################################
'''								FUNCTIONS THAT CHECK C CODE NOT FOR COMMENTS											  '''
#############################################################################################################################

#this section of functions will usually be in three sections because
#we need to make sure the string for is in the line as a forloop
#and not just inside of some kind of comment
#block comment case is if the line contains a block comment
#line comment case is if the line contains a line comment
#normal case if the line is just a line on its own
 
""" 
	cForCheck(myLine)
	this is a function to check c Code
	this function will be checking c code line for for loop statements
    
    pre myLine is a line of code
    
    returns true if the line is a forloop statment false otherwise
"""
def cForCheck(myLine):
    blkCom = '/*'
    lineCom = '//'
    rFor = 'for'
    theCol = ';'
    #this is the block comment case
    if blkCom in myLine:
        if rFor in myLine and theCol in myLine and myLine.index(rFor) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if rFor in myLine and theCol in myLine and myLine.index(rFor) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case 
    elif rFor in myLine and theCol in myLine:
        return True
    else:
        return False

""" 
	cIfCheck(myLine)
	this is a function to check c Code
	this function will be checking c code line for if statements
    
    pre myLine is a line of code
    
    returns true if the line is an if statment false otherwise
"""
def cIfCheck(myLine):
    rIf = 'if'
    rElse = 'else'
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if (rIf in myLine or rElse in myLine) and myLine.index(rIf) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if (rIf in myLine or rElse in myLine) and myLine.index(rIf) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case 
    elif (rIf in myLine or rElse in myLine):
        return True
    else:
        return False

""" 
	cColsCheck(myLine)
	this is a function to check c Code
	this function will be checking c code line for existence of colons
	
	pre myLine is a line of code
    
    returns true if ';' is in the line myLine false otherwise
"""
def cColsCheck(myLine):
    cols = ';'
    blkCom = '/*'
    lineCom = '//'
	#this is the block comment case
    if blkCom in myLine:
        if cols in myLine and myLine.index(cols) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if cols in myLine and myLine.index(cols) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case 
    elif cols in myLine:
        return True
    else:
        return False

""" 
	cDeclarSimpleCheck(myType,myLine)
	this is a function to check c Code
	this function will be checking c code line to see if it is a simple type declaration of a primitive variable
    
    pre myLine is a line of code
		myType is a list containing strings of primitive variables
    
    returns true if the line is any of the variables that are primitive type decs , false otherwise
"""
def cDeclarSimpleCheck(myType,myLine):
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
		for a in myType:
			if a in myLine and myLine.index(a) < myLine.index(blkCom):
				return True
		else:
			return False
	#this is the line comment case
    elif lineCom in myLine:
        for a in myType:
            if a in myLine and myLine.index(a) < myLine.index(lineCom):
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

""" 
	cWhileCheck(myLine)
	this is a function to check c Code
	this function will be checking c code line to see if it is a while loop statment
    
    pre myLine is a line of code
    
	returns true if the line is a while loop statment , false otherwise
"""
def cWhileCheck(myLine):
    theWhile = 'while'
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if theWhile in myLine and myLine.index(theWhile) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if theWhile in myLine and myLine.index(theWhile) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case 
    elif theWhile in myLine:
        return True
    else:
        return False

""" 
	cFunctionHeaderCheck(myLine,simpleFunctionTypes)
	this is a function to check c Code
	this function will be checking c code line to see if it is a function header
    
    pre myLine is a line of code
    	simpleFunctionTypes is a list of strings containing common function return types
    
    returns true if the line is a function Header, false otherwise
"""
def cFunctionHeaderCheck(myLine,simpleFunctionTypes):
    brackOpen = '('
    brackClose = ')'
    blkCom = '/*'
    lineCom = '//'
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
        if blkCom in myLine:
            for a in simpleFunctionTypes:
                if a in myLine and myLine.index(a) < myLine.index(brackOpen) and myLine.index(a) < myLine.index(blkCom):
                    return True
            else:
                return False
        #this is the line comment case
        elif lineCom in myLine:
            for a in simpleFunctionTypes:
                if a in myLine and myLine.index(a) < myLine.index(brackOpen) and myLine.index(a) < myLine.index(lineCom):
                    return True
            else:
                return False
        #this is the normal case 
        else:
            for a in simpleFunctionTypes:
                if a in myLine and myLine.index(a) < myLine.index(brackOpen):
                    return True
            else:
                return False
    return False

"""
    cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an openiong bracket on the line
    
    pre myLine is a line of code
    
    returns true if the line is a an open bracket, false otherwise
"""
def cBlockBracketOpen(myLine):
    brack = '{'
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if brack in myLine and myLine.index(brack) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if brack in myLine and myLine.index(brack) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case
    elif brack in myLine:
        return True
    else:
        return False

"""
    cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an closing bracket on the line
    
    pre myLine is a line of code
    
    returns true if the line is a close bracket, false otherwise
"""
def cBlockBracketClose(myLine):
    brack = '}'
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if brack in myLine and myLine.index(brack) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if brack in myLine and myLine.index(brack) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case
    elif brack in myLine:
        return True
    else:
        return False

"""
    cBlockBracketOpen(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an include statment on the line
    
    pre myLine is a line of code
    
    returns true if the line is a for libraries in the program, false otherwise
"""
def cLibraryIncludes(myLine):
    poundSign = '#'
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if poundSign in myLine and myLine.index(poundSign) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if poundSign in myLine and myLine.index(poundSign) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case
    elif poundSign in myLine:
        return True
    else:
        return False

"""
    cStructChecker(myLine)
    this is a function to check c Code
    this function will be checking c code line to see if there is an structs on the line
    
    pre myLine is a line of code
    
    returns true if the line is a for structs in the program, false otherwise
"""
def cStructChecker(myLine):
    structor = 'struct '
    blkCom = '/*'
    lineCom = '//'
    #this is the block comment case
    if blkCom in myLine:
        if structor in myLine and myLine.index(structor) < myLine.index(blkCom):
            return True
        else:
            return False
    #this is the line comment case
    elif lineCom in myLine:
        if structor in myLine and myLine.index(structor) < myLine.index(lineCom):
            return True
        else:
            return False
    #this is the normal case
    elif structor in myLine:
        return True
    else:
        return False