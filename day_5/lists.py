# Day 5

empty_list = list

more_than_5 = [1, 2, 3, 4, 5, 6]

print(len(more_than_5))

print(more_than_5[0], more_than_5[len(more_than_5) // 2], more_than_5[-1])

mixed_list = ['Juan', 17, 175, 'Single', 'Jerez']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

it_companies[1] = 'Xiaomi'
print(it_companies)

it_companies.append('Google')

it_companies = it_companies[0:len(it_companies) // 2] + ['Acer'] + it_companies[len(it_companies) // 2:]

it_companies[0] = it_companies[0].upper()

it_companies_hash = '#'.join(it_companies)

print('IBM' in it_companies)

it_companies.sort()

it_companies.reverse()

it_companies = it_companies[2:]

it_companies = it_companies[:len(it_companies) - 3]

it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]

it_companies.pop(0)

it_companies.pop(len(it_companies) // 2)

it_companies.pop(len(it_companies) - 1)

it_companies.clear()

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
front_end.append(back_end)

full_stack = front_end
indx = full_stack.index('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]