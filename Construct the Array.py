#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countArray' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER x
#

def countArray(n, k, x):
    limit = (pow(10, 9)+7)
    if k < 2:
        return 0
    if n == 3:
        return sum([1 for i in range(1,k+1) if ((i != 1)and(i != x))] )
    # Return the number of ways to fill in the array.
    
    oneValueAtMemo = [None]*(n+1)
    kMinus2AtMemo = [None]*(n+1)
    kMinus1AtMemo = [None]*(n+1)
    
    stack = [(1, n)]
    
    sumS = 0
    
    oneValue = 1
    kMinus2 = 2
    kMinus1 = 3
    
    
    while len(stack) > 0:
        #print(stack)
        (ki, ni) = stack[-1]
        
        if ki == oneValue:
            if ni == 2:
                stack.pop()
                try:
                    oneValueAtMemo[ni] =  1 if x != 1 else 0
                except MemoryError:
                    print("oneValueAtMemo")
                        
                #print("oneValueAtMemo[", ni, "] = ", oneValueAtMemo[ni])
            else:
                if kMinus2AtMemo[ni - 1] is None:
                    stack.append( (kMinus2, ni-1))
                else:
                    if kMinus1AtMemo[ni - 1] is None:
                        stack.append( (kMinus1, ni -1))
                    else:
                        stack.pop()
                        try:
                            tempval = (kMinus2AtMemo[ni - 1] + kMinus1AtMemo[ni - 1])
                            if tempval > limit:
                                tempval  = tempval % limit
                            oneValueAtMemo[ni] = tempval
                        except MemoryError:
                            print("oneValueAtMemo 2")
                        #print("oneValueAtMemo[", ni, "] = ", oneValueAtMemo[ni])
    
        
        if ki == kMinus2: 
            if ni == 2:
                stack.pop()
                try:
                    kMinus2AtMemo[ni] = 0 if x==1 else k - 2
                except MemoryError:
                    print("kMinus2AtMemo 1")
                #print("kMinus2AtMemo[", ni, "] = ", kMinus2AtMemo[ni])
            else:
                if kMinus2AtMemo[ni - 1] is None:
                    stack.append( (kMinus2, ni-1))
                else:
                    if kMinus1AtMemo[ni - 1] is None:
                        stack.append( (kMinus1, ni -1))
                    else:
                        stack.pop()
                        try:
                            tempval = (k-2)*(kMinus2AtMemo[ni - 1] + kMinus1AtMemo[ni - 1])
                            if tempval > limit:
                                tempval  = tempval % limit
                            kMinus2AtMemo[ni] = tempval
                        except MemoryError:
                            print("kMinus2AtMemo 2")
                        #print("kMinus2AtMemo[", ni, "] = ", kMinus2AtMemo[ni])
                
        if ki == kMinus1: 
            if ni == 2:
                stack.pop()
                try:
                    kMinus1AtMemo[ni] = k-1 if x==1 else 0
                except MemoryError:
                    print("kMinus1AtMemo 1")
                #print("kMinus1AtMemo[", ni, "] = ", kMinus1AtMemo[ni])
            else:
                if oneValueAtMemo[ni - 1] is None:
                    stack.append( (oneValue, ni -1))
                else:
                    stack.pop()
                    try:
                        tempval = (k-1)*(oneValueAtMemo[ni - 1])
                        if tempval > limit:
                            tempval  = tempval % limit
                        kMinus1AtMemo[ni] = tempval
                    except MemoryError:
                        print("kMinus1AtMemo 2 ", oneValueAtMemo[ni - 1])
                    #print("kMinus1AtMemo[", ni, "] = ", kMinus1AtMemo[ni])
                    
                
    return oneValueAtMemo[n]
    
 #   def oneValueAt(ni):
 #       if oneValueAtMemo[ni] is not None:
 #           return oneValueAtMemo[ni]
 #       if ni == 1:
 #           oneValueAtMemo[ni] =  1 if x != 1 else 0
 #       else:            
 #           oneValueAtMemo[ni] =  kMinus2At(ni-1) + kMinus1At(ni-1)
 #       return oneValueAtMemo[ni]
 #           
 #   def kMinus2At(ni):
 #       if kMinus2AtMemo[ni] is not None:
 #           return kMinus2AtMemo[ni]
 #       if ni == 1:
 #           kMinus2AtMemo[ni] = 0 if x==1 else k - 2
 #       else:
 #           kMinus2AtMemo[ni] =  (k-2)*(kMinus2At(ni-1) + kMinus1At(ni-1))
 #       return kMinus2AtMemo[ni]
 #           
 #   def kMinus1At(ni):
 #       if kMinus1AtMemo[ni] is not None:
 #           return kMinus1AtMemo[ni]
 #       if ni == 1:
 #           kMinus1AtMemo[ni] = k-1 if x==1 else 0
 #       else:
 #          kMinus1AtMemo[ni] =  (k-1) * oneValueAt(ni-1)
 #      return kMinus1AtMemo[ni]
 #      
 #  return (kMinus2At(n-2) + kMinus1At(n-2)) % limit
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split() 

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = int(first_multiple_input[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()
