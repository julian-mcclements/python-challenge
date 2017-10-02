"Decipher message encrypted with Caesar cypher."

# http://www.pythonchallenge.com/pc/def/map.html

class Decrypter:
    "Caesar cypher initialised for solving challenge."

    def __init__(self):
        self.decypher = {
            'a':'c',
            'b':'d',
            'c':'e',
            'd':'f',
            'e':'g',
            'f':'h',
            'g':'i',
            'h':'j',
            'i':'k',
            'j':'l',
            'k':'m',
            'l':'n',
            'm':'o',
            'n':'p',
            'o':'q',
            'p':'r',
            'q':'s',
            'r':'t',
            's':'u',
            't':'v',
            'u':'w',
            'v':'x',
            'w':'y',
            'x':'z',
            'y':'a',
            'z':'b'}

    def __reverse(self, cypher_char):
        "Reverse shift to get plain"
        return self.decypher[cypher_char]

    def decrypt(self, cypher_text):
        "Decypher encrypted text"
        # Split string into list of single characters.
        cypher_chars = list(cypher_text)
        plain_text = []
        for char in cypher_chars:
            plain_text.append(self.__reverse(char) if char.isalpha() else char)
        # Join list to create single string.
        return "".join(plain_text)

def challenge01():
    "Function implementing answer."

    # Inefficient way of setting up decryption
    # decrypter = Decrypter()

    intab = "abcdefghijklmnopqrstuvwxyz"
    outtab = "cdefghijklmnopqrstuvwxyzab"
    translation_table = str.maketrans(intab, outtab)

    # Define multiline string with not trailing white-space.
    cyphertext = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
                  "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle."
                  "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

    # Inefficient way of setting up decryption
    # result = decrypter.decrypt(cyphertext)

    plaintext = cyphertext.translate(translation_table)
    print(plaintext)
    print("http://www.pythonchallenge.com/pc/def/%s.html" % "map".translate(translation_table))

    return

if __name__ == "__main__":
    challenge01()
