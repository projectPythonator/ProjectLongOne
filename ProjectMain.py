if __name__ == '__main__':
    typeOfCode = raw_input("what type of code will you be using?(c,p,j)\n")
    if typeOfCode == 'c':
        import cMainFile
        cMainFile.cMain()
    elif typeOfCode == 'j':
        import javaMainFile
        javaMainFile.javaMain()
    elif typeOfCode == 'p':
        import pythonMainFile
        pythonMainFile.pythonMain()
		
