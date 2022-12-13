# Day 3

age = 17

height = float(175)

c_number = complex(2, 5)

print("Area of the triangle:", 0.5 * int(input('Base: ')) * int(input('Height: ')))

print("Perimeter of the triangle:", int(input('a: ')) + int(input('b: ')) + int(input('c: ')))

length = int(input('Enter length: '))
width = int(input('Enter width: '))
print('Area: ', length * width)
print('Perimeter: ', 2 * (length + width))

radius = int(input('Enter radius: '))
print('Area:', 3.14 * radius * radius)
print('Circunference', 2 * 3.14 * radius)

print("X intercept: ", 1)
print("Y intercept: ", -2)
print("Slope: ", 2)

x1, x2, y1, y2 = 2, 6, 2, 10
print('Distance: ')
print('{0:.2f}'.format(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
print('Slope:')
print((y2 - y1) / (x2 - x1))

print(2 if 2 < (y2 - y1) / (x2 - x1) else (y2 - y1) / (x2 - x1))

for x in range(0, 10):
    print(x ** 2 + 6 * x + 9)
print(3, -3, "is where y is 0")

print(not len('python') == len('dragon'))

print('on' in 'python' and 'on' in 'dragon')

print('jargon' in "I hope this course is not full of jargon")

print('on' not in 'python' and 'on' in 'dragon')

print(str(float(len('python'))))

number = int(input('Enter number:'))
print("Even" if number % 2 == 0 else "Odd")

print(type('10') == type(10))

hours = int(input('Enter hours:'))
rph = int(input('Enter rate per hour:'))
print("Weekly Earning:", hours * rph)

years = int(input('Enter years:'))
print(years * 365 * 24 * 60 * 60 * 60)

for i in range(1, 6):
    print(i, i ** 0, i ** 1, i ** 2, i ** 3)