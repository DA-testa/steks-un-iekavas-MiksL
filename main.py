# python3

from collections import namedtuple
import os

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


# Use an input to choose files or input - F or I (Capital i) If input I, wait for user to input a string manually
def main():
    #print("Choose an input method: F - Existing test from the test folder, I - Manual input"")
    text = input()
    if(text == "F"):
        # Read the text from the test files in the "test" folder, get a ilst of the files and present a choice to the user
        files = os.listdir("test")
        
        #print("Choose a file to use as as a test input case from 0-5:")
        
        # Get the user input and convert it to an integer
        chosen_input_file = int(input())
        
        # Open the file, read the first line and pass it to the find_mismatch function for processing
        text = open("test/" + files[chosen_input_file], "r").readline()
    elif(text == "I"):
        text = input() # Gets whatever the user is willing to input
    else:
        print("Invalid input")
        return # A return is placed so a false find_mismatch result is not output after the Invalid input message
        
    mismatch = find_mismatch(text)
    print(mismatch) # Output the result of the find_mismatch function


if __name__ == "__main__":
    main()
