import os
from InputClass import InputCLass


def getFileDirc():
    sdir = os.path.dirname(os.path.abspath(__file__)).split(os.sep)[-1]
    sdir = sdir+"/HellowWorkdd.c"
    return sdir

def getUserInput():
    print("please enter the header for the function you would like start from?")
    my_header = raw_input()
    return my_header

def main():
    the_script = getFileDirc()
    the_header = getUserInput()
    ourInputs = InputCLass(the_header,the_script)
    print("i did input")



if __name__ == '__main__':
    main()
