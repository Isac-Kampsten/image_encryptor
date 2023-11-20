def stringToBinary(message):
    string = ""
    for i in message:
        string += (format(ord(f"{i}"), '08b'))
    return string


