#!/usr/bin/python
# -*- coding: utf-8 -*-

def checkio(f,g):

    # Replace with your code
    def h(*args,**kwargs):
        f_err = g_err = False
        try:
            f_result = f(*args, **kwargs)
        except:
            f_err = True
            f_result = None
        try:
            g_result = g(*args, **kwargs)
        except:
            g_err = True
            g_result = None
        print("f_result: {}".format(f_result))
        print("g_result: {}".format(g_result))
        print("f_err: {}".format(f_err))
        print("g_err: {}".format(g_err))
        if f_err and g_err:
            return (None, 'both_error')
        if f_err and g_result:
            return (g_result, 'f_error')
        if g_err and f_result:
            return (f_result, 'g_error')
        if None == f_result:
            if not None == g_result:
                return (g_result, 'f_error')
            else:
                return (None, 'both_error')
        if None == g_result:
            return (f_result, 'g_error')
        if f_result != g_result:
            return (f_result, 'different')
        return (f_result, 'same')
        if f_result == g_result:
            return (f(*args, **kwargs), 'same')
        #return (f(*args,**kwargs),'same')
    return h

if __name__ == '__main__':
       
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    # (x+y)(x-y)/(x-y)
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,3)==(4,'same'), "Function: x+y, first"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,2)==(3,'same'), "Function: x+y, second"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1.01)==(2.01,'different'), "x+y, third"
    assert checkio(lambda x,y:x+y,    
                   lambda x,y:(x**2-y**2)/(x-y))\
                   (1,1)==(2,'g_error'), "x+y, fourth"

    # Remove odds from list               
    f = lambda nums:[x for x in nums if ~x%2]
    def g(nums):
      for i in range(len(nums)):
        if nums[i]%2==1:
          nums.pop(i)
      return nums 
    assert checkio(f,g)([2,4,6,8]) == ([2,4,6,8],'same'), "evens, first"
    assert checkio(f,g)([2,3,4,6,8]) == ([2,4,6,8],'g_error'), "evens, second"         
    
    # Fizz Buzz    
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (6)==('Fizz','same'), "fizz buzz, first"      
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (30)==('Fizz Buzz','same'), "fizz buzz, second"
    assert checkio(lambda n:("Fizz "*(1-n%3) + "Buzz "*(1-n%5))[:-1] or str(n),
                   lambda n:('Fizz'*(n%3==0) + ' ' + 'Buzz'*(n%5==0)).strip())\
                   (7)==('7','different'), "fizz buzz, third"

