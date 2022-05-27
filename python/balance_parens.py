def balance_parens(str):
    # array for indices of right parens unmatched with left parens	
    loneRight = []
    # array for indices of right parens, matched or not	
    stack = []
    for i in range(0, len(str)):
        # if left paren, push index to stack	
        if str[i] == '(':
            stack.append(i)
        elif str[i] == ')':
            # if unmatched right paren, push index to array
            if len(stack) == 0:
                loneRight.append(i)
            #otherwise, remove corresponding left paren
            else:
                stack.pop()
    # split into array of characters
    str = list(str)
    # concat to create array of unmatched left and right parens
    loneRight = loneRight + stack
    # iterate and replace unmatched left and right parens with ''
    for j in range(0, len(loneRight)):
        str[loneRight[j]] = ''
    # join array into string and return
    return ''.join(str)
#print(balance_parens(")(())("))    