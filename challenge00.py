"Calculate 2 to the power of 38."

# http://www.pythonchallenge.com/pc/def/0.html

def challenge00():
    "Function implementing answer."
    val = 2
    exponent = 38
    # 2 is already 2 raised to the power of 1
    result = val << (exponent - 1)
    print("http://www.pythonchallenge.com/pc/def/%d.html" % result)
    return

if __name__ == "__main__":
    challenge00()
