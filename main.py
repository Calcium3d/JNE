def encryption(unencrypted_text):
    unencrypted_text = unencrypted_text.lower()
    unencrypted_text[:0] = unencrypted_text
    unencrypted_text = list(unencrypted_text)

    for letter in unencrypted_text:
        if letter == "a":
            letter = "s"
        
        elif letter == "b":
            letter = "n"
        
        elif letter == "c":
            letter = "m"

        elif letter == "d":
            letter = "f"

        elif letter == "e":
            letter = "r"
        
        elif letter == "f":
            letter = "g"
        
        elif letter == "g":
            letter = "h"

        elif letter == "h":
            letter = "j"

        elif letter == "i":
            letter = "o"

        elif letter == "j":
            letter = "k"

        elif letter == "k":
            letter = "l"

        elif letter == "l":
            letter = ";"

        elif letter == "m":
            letter = ","

        elif letter == "n":
            letter = "m"

        elif letter == "o":
            letter = "p"

        elif letter == "p":
            letter = "["

        elif letter == "q":
            letter = "w"

        elif letter == "r":
            letter = "t"

        elif letter == "s":
            letter = "d"

        elif letter == "t":
            letter = "y"

        elif letter == "u":
            letter = "i"

        elif letter == "v":
            letter = "b"

        elif letter == "w":
            letter = "e"

        elif letter == "x":
            letter = "c"

        elif letter == "y":
            letter = "u"

        elif letter == "z":
            letter = "x"

        elif letter == "`":
            letter = "~"

        elif letter == "1":
            letter = "!"

        elif letter == "2":
            letter = "@"

        elif letter == "3":
            letter = "#"

        elif letter == "4":
            letter = "$"

        elif letter == "5":
            letter = "%"

        elif letter == "6":
            letter = "^"

        elif letter == "7":
            letter = "&"

        elif letter == "8":
            letter = "*"

        elif letter == "9":
            letter = "("

        elif letter == "0":
            letter = ")"

        elif letter == "-":
            letter = "_"

        elif letter == "=":
            letter = "+"

        elif letter == "[":
            letter = "{"

        elif letter == "]":
            letter = "}"

        elif letter == "\\":
            letter = "|"

        elif letter == ";":
            letter = ":"

        elif letter == "'":
            letter = "\""

        elif letter == ",":
            letter = "<"

        elif letter == ".":
            letter = ">"

        elif letter == "/":
            letter = "?"

        else:
            letter = letter
    
    encrypted_text = ""
    for l in encrypted_text:
        encrypted_text += l
    
    return encrypted_text


def decryptor(encrypted_text):
    encrypted_text = encrypted_text.lower()
    encrypted_text[:0] = encrypted_text
    encrypted_text = list(encrypted_text)


for letter in unencrypted_text:
        if letter == "s":
            letter = "a"
        
        elif letter == "n":
            letter = "b"
        
        elif letter == "m":
            letter = "c"

        elif letter == "f":
            letter = "d"

        elif letter == "r":
            letter = "e"
        
        elif letter == "g":
            letter = "f"
        
        elif letter == "h":
            letter = "g"

        elif letter == "j":
            letter = "h"

        elif letter == "o":
            letter = "i"

        elif letter == "k":
            letter = "j"

        elif letter == "l":
            letter = "k"

        elif letter == ";":
            letter = "l"

        elif letter == ",":
            letter = "m"

        elif letter == "m":
            letter = "n"

        elif letter == "p":
            letter = "o"

        elif letter == "[":
            letter = "p"

        elif letter == "w":
            letter = "q"

        elif letter == "t":
            letter = "r"

        elif letter == "d":
            letter = "s"

        elif letter == "y":
            letter = "t"

        elif letter == "i":
            letter = "u"

        elif letter == "b":
            letter = "v"

        elif letter == "e":
            letter = "w"

        elif letter == "c":
            letter = "x"

        elif letter == "u":
            letter = "y"

        elif letter == "x":
            letter = "z"

        elif letter == "~":
            letter = "`"

        elif letter == "!":
            letter = "1"

        elif letter == "@":
            letter = "2"

        elif letter == "#":
            letter = "3"

        elif letter == "$":
            letter = "4"

        elif letter == "%":
            letter = "5"

        elif letter == "^":
            letter = "6"

        elif letter == "&":
            letter = "7"

        elif letter == "*":
            letter = "8"

        elif letter == "(":
            letter = "9"

        elif letter == ")":
            letter = "0"

        elif letter == "_":
            letter = "-"

        elif letter == "+":
            letter = "="

        elif letter == "{":
            letter = "["

        elif letter == "}":
            letter = "]"

        elif letter == "|":
            letter = "\\"

        elif letter == ":":
            letter = ";"

        elif letter == "\"":
            letter = "'"

        elif letter == "<":
            letter = ","

        elif letter == ">":
            letter = "."

        elif letter == "?":
            letter = "/"

        else:
            letter = letter
    
    unencrypted_text = ""
    for l in unencrypted_text:
        uncrypted_text += l
    
    export unencrypted_text

def main():
    print("Welcome to JNE")

    print("Would you like to encrypt or decrypt? (encrypt/decrypt)")
    choice = input("=> ")

    if choice == "encrypt":
        answer = encryption(choice)

    if choice =="decrypt":
        answer = decryptor(choice)

    print("Your string is: {}".format(answer))


