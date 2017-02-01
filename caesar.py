import string

def alphabet_position(char, ABC):
    return ABC.index(char)

def rotate_character(char, rot):
    if not char.isalpha():
        return char
    ABC = string.ascii_uppercase if char.isupper() else string.ascii_lowercase
    x = alphabet_position(char,ABC)
    sum = (x + rot) % len(ABC)
    return(ABC[sum])

def encrypt(text, rot):
    #ntxt = ''
    #for char in text:
    #    ntxt += rotate_character(char, rot)
    #return ntxt
    nlst = []
    for char in text:
        nlst.append(rotate_character(char, rot))
    return "".join(nlst)
