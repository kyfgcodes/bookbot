test = {'p': 6121, 'r': 20818, 'o': 25225, 'j': 504, 'e': 46043, 'c': 9243, '*': 28, 'z': 243, '?': 220, ';': 970, 'x': 677, 'q': 324, '!': 239, '"': 796, '3': 18, '5': 16, '9': 13, '6': 10, '_': 2, '/': 24, '%': 1, '@': 2, '$': 2}


for key in sorted(test, key=test.get, reverse=True):
        if key.isalpha():

          print(f"the key name is {key} and its value is {test[key]}")
  