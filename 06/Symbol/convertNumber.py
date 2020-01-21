# https://stackoverflow.com/questions/22746429/c-decimal-to-binary-converting
def getBinary(decimal, binary):
    if decimal // 2 != 0:
        getBinary(decimal // 2, binary)
    binary.append(decimal % 2)
