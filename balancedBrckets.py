from stack import Stack

left = ['(', '<', '[', '{']
right = [')', '>', ']', '}']


def isMatched(p1, p2):
    return


def is_balanced(paren_string):
    s = Stack()
    for str in paren_string:
        if str in left:
            s.push(str)

        if str in right:
            if s.is_empty:
                return False
            top = s.pop()
            if(top)
