# Day 7

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

it_companies.update(['PCComponentes', 'Xiaomi'])

it_companies.remove('Xiaomi')

'''si el elemento que quiero quitar no está en el set y uso remove(), da un error'''

print(A.union(B))

print(A.intersection(B))

print(A.issubset(B))

print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))

del A
del B