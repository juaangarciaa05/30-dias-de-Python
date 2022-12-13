# Day 4

a= "Thirty"
b= "days"
c= "of"
d= "Python"
space= " "
print(a+space+b+space+c+space+d)

e= "Coding"
f= "for"
g= "all"
print(e+space+f+space+g)

company= "Coding for all"

print(company)

print(len(company))

print(company.upper())

print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[7:])

print(company[company.index("Coding"):7])

print(company.replace("Coding","Python"))

print('Python for Everyone'.replace("Everyone", "All"))

print(company.split())

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))

print(company[0])

print(company[-1])

print(company[10])

words= 'Python For Everyone'.split()
print(words[0][0] + words[1][0] + words[2][0])

words= 'Coding For All'.split()
print(words[0][0] + words[1][0] + words[2][0])

print("Coding For All".index('C'))

print("Coding For All".index('F'))

print("Coding For All People".rfind('1'))

sentence='You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

print(sentence.rfind('because'))

print(sentence.replace('because because because', ''))


