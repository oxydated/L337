def postOrder(root):
    #Write your code here
    stack = [(root, False)]
    result = []
    while len(stack) > 0:
        (node, visited) = stack.pop()
        if visited or (node.left is None and node.right is None):
            result.append(node.info)
        else:
            childRight = node.right
            childLeft = node.left
            stack.append((node, True))
            if childRight:
                stack.append((childRight, False))
            if childLeft:
                stack.append((childLeft, False))
    resultStr = ""
    for i in result:
        resultStr+=(str(i)+" ")
    print(resultStr)
