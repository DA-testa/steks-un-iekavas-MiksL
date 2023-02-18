# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


# find_mismatch - should find if a bracket is missing or if there is a mismatch in the type of brackets being used
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # We place the opening bracket in the opening_brackets_stack list so it can be checked later once the closing brackets are found
            opening_brackets_stack.append(next)
            pass

        if next in ")]}":
            # We check if the stack is empty, if it is then there is a mismatch (no opening bracket)
            if(len(opening_brackets_stack) == 0):
                return i+1
            else: # If the stack is not empty we check if the opening bracket matches the last bracket in the stack (because the last opening bracket has to be closed first)
                if(are_matching(opening_brackets_stack.pop(), next) == False):
                    return i+1
            pass
    
    # After the loop check if the stack is empty (empty = there were no mismatches), if it is not then we return the position of the first unmatched opening bracket
    if(len(opening_brackets_stack) != 0):
        return opening_brackets_stack[0].position + 1
    else: # Else is not necessary here but it helps with readability
        return "Success" # We return success if no mismatches were found during the execution of the loop and the stack is empty


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch) # Output the result of the find_mismatch function


if __name__ == "__main__":
    main()
