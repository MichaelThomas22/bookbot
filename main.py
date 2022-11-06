with open("books/Frankenstein.txt") as f:
    file_contents = f.read()
words = file_contents

def countwords(mystring):
    mystring = mystring.lower()
    lcount = {}
    allowedchar = set('abcdefghijklmnopqrstuvwxyz')
    mystring = ''.join(filter(allowedchar.__contains__,mystring))
    for l in mystring:
        if l in lcount:
            lcount[l] += 1
        else:
            lcount[l] = 1
    return lcount

print(countwords(words))