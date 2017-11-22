#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(expression):
    left = "([{"
    right = ")]}"
    match = {"(":")","[":"]", "{":"}"}
    st = []
    #print ("expression = {}".format(expression))
    for c in expression:
        if c in left:
            st.append(c)
            #print ("c = {}, stack = {}".format(c, st))
            
        if c in right:
            try:
                top = st.pop()
                #print("c = {}, top = {}, match[top] = {}, stack = {}".format(c, top, match[top], st))
                if not c == match[top]:
                    return False
            except:
                #print(c)
                return False
    if not len(st):
        return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
