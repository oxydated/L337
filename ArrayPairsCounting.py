#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def solve(arr):
    # Write your code here
    class node:
        def __init__(self, value, position):
            self.value = value
            self.position = position
            self.left = None
            self.right = None
            self.parent = None
            self.treeSize = 1
            
    class BST:
        def __init__(self):
            self.root = None
        
        def insertNode(self, value, position):
            if self.root is None:
                self.root = node(value, position)
            else:
                if value >= self.root.value:
                    oldRoot = self.root
                    self.root = node(value, position)
                    if oldRoot.position > self.root.position:
                        self.root.right = oldRoot
                    else:
                        self.root.left = oldRoot
                else:
                    newNode = node(value, position)
                    currentNode = self.root
                    while currentNode is not None:
                        if newNode.position > currentNode.position:
                            currentChild = currentNode.right
                        else:
                            currentChild = currentNode.left
                        if currentChild is None or newNode.value >= currentChild.value:
                            if newNode.position > currentNode.position:
                                currentNode.right = newNode
                            else:
                                currentNode.left = newNode
                            if currentChild is not None:
                                currentNode = newNode
                                newNode = currentChild
                            else:
                                currentNode = None
                        else:
                            currentNode = currentChild
        
        def updateTreeSize(self):
            if self.root:
                stack = [(self.root, False)]
                while len(stack) > 0:
                    (currentNode, visited) = stack.pop()
                    if visited:
                        currentNode.treeSize += currentNode.left.treeSize if currentNode.left else 0
                        currentNode.treeSize += currentNode.right.treeSize if currentNode.right else 0
                    else:
                        stack.append((currentNode, True))
                        if currentNode.right:
                            stack.append((currentNode.right, False))
                        if currentNode.left:
                            stack.append((currentNode.left, False))
        
        def getNumPairsForNode(maxNode:node):
            stack = [maxNode]
            numPairs = 0
            while len(stack) > 0:
                currentNode = stack.pop()
                key = math.floor( maxNode.value / currentNode.value)
                startArray = maxNode if currentNode.position > maxNode.position else maxNode.left
                startStack = []
                if startArray:
                    startStack.append(startArray)
                currentStartNode = None
                while len(startStack)> 0:
                    currentStartNode = startStack.pop()
                    if currentStartNode.value <= key:
                        numPairs += currentStartNode.treeSize if currentStartNode else 0
                        #print("maxNode: ", maxNode.position + 1, "pair: (", currentStartNode.position + 1, ", ", currentNode.position + 1, "), numPairs: ", numPairs)
                    else:
                        if currentStartNode.left:
                            startStack.append(currentStartNode.left)
                        if currentStartNode.right and currentStartNode.right.position < maxNode.position:
                            startStack.append(currentStartNode.right)
                if currentNode.left and currentNode.left.position > maxNode.position:
                    stack.append(currentNode.left)
                if currentNode.right:
                    stack.append(currentNode.right)
            return numPairs
                    
                
            
        
    tree = BST()          
    for pos, value in enumerate(arr):
        tree.insertNode(value, pos)
    tree.updateTreeSize()
    #print("BST complete")
    stack = [(tree.root, False)]
    numPairs = 0
    while len(stack) > 0:
        (currentNode, visited) = stack.pop()
        if visited:
            numPairsForNode = BST.getNumPairsForNode(currentNode)
            numPairs += numPairsForNode
            #print(currentNode.value, " {", currentNode.position + 1, "} ", "[", currentNode.treeSize, "] ", "numPairs: ", numPairsForNode)
        else:
            if currentNode.right:
                stack.append((currentNode.right, False))
            stack.append((currentNode, True))
            if currentNode.left:
                stack.append((currentNode.left, False))
    return numPairs
      
                    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = solve(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
