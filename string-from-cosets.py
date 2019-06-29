# return a string from a list of cosets
# should return "axjqbykrczls"

a = ["a", "b", "c"]
b = ["x", "y", "z"]
c = ["j", "k", "l"]
d = ["q", "r", "s"]
chars = [a, b, c, d]

def coset_to_str(coset_list):
    """ returns reformed string from cosets """
    newstr = []
    try:
        for i in range(len(coset_list)):
            for j in chars:
                newstr.append(j[i])
    except IndexError:
        pass

    return "".join([i for i in newstr])

## test
#print(coset_to_str(chars))
