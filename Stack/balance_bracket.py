from stack import Stack
def is_matched(open_bracket: str, close_bracket: str) -> bool:
    if open_bracket == '(' and close_bracket == ')':
        return True
    elif open_bracket == '[' and close_bracket == ']':
        return True
    elif open_bracket == '{' and close_bracket == '}':
        return True
    else:
        return False

def is_paren_balanced(input: str) -> bool:
    s = Stack()
    open_brackets = '([{'
    if not input:
        print('Input is empty')
        return False
    else:
        for i in input:
            if i in open_brackets:
                s.push(i)
            else:
                if s.is_empty():
                    return False
                else:
                    top = s.pop()
                    if is_matched(top,i):
                        continue
                    else:
                        return False

    return True



print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))