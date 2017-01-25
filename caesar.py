
def alphabet_position(letter):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uplo = ""
    x = 0
    if ABC.find(letter) > -1:
        x = ABC.find(letter)
        uplo = "UP"
    else:
        let = letter.upper()
        if ABC.find(let) > -1:
            x = ABC.find(let)
            uplo = "lo"
    return (x, uplo)

def rotate_character(char, rot):
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    p_c = alphabet_position(char)
    sum = (p_c[0] + rot) % 26
    if p_c[1] == "lo":
        return (ABC[sum].lower(),True)
    elif p_c[1] == "UP":
        return(ABC[sum],True)
    else:
        return (char,False)

def encrypt(text, rot):
    ntxt = ''
    for i in range(len(text)):
        char_bool = rotate_character(text[i], rot)
        ntxt += char_bool[0]
    return ntxt
