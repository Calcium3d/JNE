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
    for l in unencrypted_text:
        encrypted_text += l
    
    return encrypted_text

