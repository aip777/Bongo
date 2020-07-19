
dictionary = {'key1': 1, 'key2': { 'key3': 1, 'key4': { 'key5': 4 }}}

def print_depth(param, run=0):
    for key, value in param.items():
        print(key, run + 1)
        if isinstance(value, dict):
            print_depth(value, run=run+1)
print_depth(dictionary)


