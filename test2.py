def stringToBinary(message):
    arr = []
    for i in message:
        arr.append((format(ord(f"{i}"), '08b')))
    return arr

print(stringToBinary("banan"))