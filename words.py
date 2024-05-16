def print_upper_words(words):
    """Print each word on a separate line, all uppcased letters"""

    for capital in words:
        print(capital.upper()) #upper makes words uppercase

# print(print_upper_words("hey"))
#H
#E
#Y

def print_e_words(words):
    """Print each word on a seperate line, all uppercased letters.
        Only print words if they start with the letter E"""
    
    for easy in words:
        if easy.startswith("e") or easy.startswith("E"):
            print(easy.upper())

# This one needs to be in [] in order to work. quotations don't work
#print(print_e_words(["eagle", "Edward", "Alfred"]))
# EAGLE
# EDWARD

def print_first_letter(words, must_start_with):
    """only print words with capitals of letters given"""

    for first in words:
        for letter in must_start_with:
            if first.startswith(letter):
                print(first.upper())
                break

# print_first_letter(["hello", "hey", "goodbye", "yo", "yes"],
            #must_start_with={"h", "y"})
#HELLO
#HEY
#YO
#YES