
from curses.ascii import isalpha, isdigit
from pickle import TRUE


def tokenize(lines):
    words = []
    for line in lines:
        start = 0
        while start < len(line):
            while line[start].isspace():
                start=start+1 

            print(line[start])
            start = start+1
    return words

   

if [] .isalpha() == TRUE:
    print ([], "letter")
elif [] .isdigit() == TRUE:
    print ([], "digit" )
else: 
    print ([], "symbol")



    
