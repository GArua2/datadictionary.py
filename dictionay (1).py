# a Dictionary is like a look up table with values stored in strings called 'keys'

dictionary= {
    "key": "value",
    "key2": 32
}

#example

ages = {
    "jaden": 12,
    "Ivy":21,
    "polycarp": "unknown"
}

print(ages['Ivy']) #prints the value 21 which is relate to the key Ivy

#CHANGING VALUE OF A KEY
ages['polycarp'] = 19
print(ages['polycarp'])

#printing all keys and values in the dictionary

##I use for loop

for key, value in ages.items():
    print('Name: ')
    print(key)
    print('Age: ')
    print(value)
    print('')

 
