from pprint import pprint

class X:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.valsum = val1 + val2


x = X(1,1)

print('Object:')
pprint(x.__dict__, indent=2)


list = ['1']

print('List:')
print(list)

list.append(x)

print('Appended list:')
print(list)

print('Appended list object:')
pprint(list[1].__dict__, indent=2)
