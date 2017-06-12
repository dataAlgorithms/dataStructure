def validateExpression(expression):

    stack = []
    pushChars, popChars = "<({[", ">)}]"
    for c in expression:
        if c in pushChars:
            stack.append(c)
        elif c in popChars:
            if not len(stack):
                return False
            else:
                stackTop = stack.pop()
                balancingBracket = pushChars[popChars.index(c)]
                if stackTop != balancingBracket:
                    return False
        else:
            return False

    return not len(stack)

'''
False
False
True
False
'''
if __name__ == '__main__':
    print validateExpression("({})))))")
    print validateExpression("({}")
    print validateExpression("({})")
    print validateExpression("({)}")
    
