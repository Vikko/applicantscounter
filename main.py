uncounters = {}
nocounters = {}
totalcount = 0

file = open('applicants.csv')
next(file) # exclude column header from counts
for line in file:
    totalcount = totalcount + 1
    un, number = line[0:2], line[2:3]
    if un not in uncounters:
        uncounters[un] = 1
    else:
        uncounters[un] += 1
    if number not in nocounters:
        nocounters[number] = 1
    else:
        nocounters[number] += 1

print('The are a total of ', totalcount, ' applicants', '.', sep = '')
print()
print('Applicants per department:')
for key,value in uncounters.items():
     print(key, value)
print()
print('Applicants per seniority level:')
for key, value in nocounters.items():
    print(key, value)
