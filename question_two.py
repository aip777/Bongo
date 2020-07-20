
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father
person_a = Person('User', '1', 'Vd')
person_b = Person('User', '2', person_a)

def con(x):
    return dict((key, getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))

dictionaryThree = {'key1': 1, 'key2': { 'key3': 1, 'key4': { 'key5': 4, 'user': person_b }}}

def print_depth(param, run=0):
    for key, value in param.items():
        print(key, run + 1)
        if isinstance(value, dict):
            print_depth(value, run=run+1)
        if isinstance(value, Person):
            if isinstance(con(value), dict):
                print_depth(vars(value), run=run + 1)
print_depth(dictionaryThree)



# key1 1
# key2 1
# key3 2
# key4 2
# key5 3
# user: 3
# first_name: 4
# last_name: 4
# father: 4
# first_name: 5
# last_name: 5
# father: 5