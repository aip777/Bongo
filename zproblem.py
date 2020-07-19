class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('4', '4','4')
person_b = Person('User', '2', person_a)

dictionaryFour = {'key1': 1, 'key2': { 'key3': 1, 'key4': { 'key5': 4, 'user':person_b, "user":{'first_name':person_b.father.first_name, "last_name":person_b.father.last_name, "father":{'first_name':person_b.father.father, "last_name":person_b.father.father, "father":person_b.father.father}}}}}

def print_depth(param, run=0):
    for key, value in param.items():
        print(key, run + 1)
        if isinstance(value, dict):
            print_depth(value, run=run+1)
print_depth(dictionaryFour)

print('\n')

print('first_name', dictionaryFour['key2']['key4']['user']['first_name'])
print('last_name', dictionaryFour['key2']['key4']['user']['last_name'])
print('father', dictionaryFour['key2']['key4']['user']['father']['father'])
