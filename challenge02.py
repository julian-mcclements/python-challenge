"Find rare characters in the mess"

# http://www.pythonchallenge.com/pc/def/ocr.html

class CharRemover:

    def __init__(self, toRemove):
        '''
        Create translation table to remove noise. This is a two-step process.

        i)  Map the characters to their ordinal values (ascii codes). The ordinal
            values are returned as a new list.
        ii) Create dictionary from list of ordinal values. Each ordinal value is 
            mapped to None because we are removing the character. This dictionary
            will be the final translation table.
        '''
        self.toRemove = dict.fromkeys(map(ord, toRemove), None)
        # (Cumulative) list of characters that were not removed.
        self.unremoved = []

    def remove(self, str):
        not_removed = list(str.strip().translate(self.toRemove))
        # Use extend method to append any elements from the list of unremoved characters.
        self.unremoved.extend(not_removed)
        
def challenge02():
    remover = CharRemover('!#$%&()*+@[]^_{}')
    filename = "ocr.txt"
    with open(filename) as f:
        # Read until EOF using readline() and returns a list containing the lines.
        content = f.readlines()
    for line in content:
        remover.remove(line)
    print("".join(remover.unremoved))

    '''
    # Remove whitespace characters like `\n` at the end of each line
    content = [line.strip() for line in content]
    # Remove non-essential characters
    content = [print(line.translate(charsToRemove)) for line in content]
    '''

if __name__ == "__main__":
    challenge02()
    