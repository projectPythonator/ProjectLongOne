import codecs
import re
import time

def javaMain():
    start_time = time.time()
    jCode = [] # this will store the code line by line in a list

    '''this portion is going to be reading in the code from a file
    it also will be checking for certain chars that may show up
    as unicode'''
    with codecs.open('myinputpuy.txt') as f: # inside of open you can put any file name with txt you want to use to test it
        jCode = [line.decode('utf-8').strip() for line in f.readlines()]
    myLength = len(jCode)
    for index in xrange(myLength):
        jCode[index] = re.sub(u"(\u2018|\u2019)", "'", jCode[index])
    print "update"
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    #call testing file for this script
    pass
