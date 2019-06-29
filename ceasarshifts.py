# returns a dict of all ceasar shifts for a text

def all_ceasars(text):
    text = text.upper()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ceasars = {}
    # loop through every possible key
    for key in range(len(letters)):
        
        translated = ''

        # shift each char in the message
        for symbol in text:
            num = letters.find(symbol)
            num = num - key

            # handle wrap around
            if num < 0:
                num = num + len(letters)

            # add num's symbol at the end of translated
            translated = translated + letters[num]
            ceasars[key] = translated

    return ceasars


### test
#for k, v in all_ceasars("hello").items():
#    print("{0:<2}: {1}".format(k,v))
