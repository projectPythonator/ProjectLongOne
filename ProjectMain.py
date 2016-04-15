import cMainFile
import javaMainFile
import pythonMainFile
if __name__ == '__main__':
	typeOfCode = raw_input("what type of code will you be using?(c,p,j)\n")
	if typeOfCode == 'c':
		cMainFile.cMain()
	elif typeOfCode == 'j':
		javaMainFile.javaMain()
	elif typeOfCode == 'p':
		pythonMainFile.pythonMain()
		