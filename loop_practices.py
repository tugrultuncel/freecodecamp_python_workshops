''' practices for loop
'''
developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        break
    print(developer)

developer_names = ['Jess', 'Naomi', 'Tom']

for developer in developer_names:
    if developer == 'Naomi':
        continue
    print(developer)

words = ['sky', 'apple', 'rhythm', 'fly', 'orange']

for word in words:
    for letter in word:
        if letter.lower() in 'aeiou':
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:
        print(f"'{word}' has no vowels")

print(range(3))

for num in range(3):
    print(num)

for num in range(1, 5):
    print(num)

for num in range(0, 5):
    print(num)

for num in range(40, 0, -10):
    print(num)

for num in range(10,0,-1):
    print(num)

numbers = list(range(1,11,1))
print(numbers)

languages = ['Spanish', 'English', 'Russian', 'Chinese']

index = 0
order = 1

for language in languages:
    print(f'Order {order}: Index {index} and language {language}')
    index += 1
    order += 1

languages = ['Spanish', 'English', 'Russian', 'Chinese']

for index, language in enumerate(languages):
    print(f'Index {index} and language {language}')

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

print(list(zip(developers, ids)))

developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
ids = [1, 2, 3, 4]

for name, dev_id in zip(developers, ids):
    print(f'Name: {name}')
    print(f'ID: {dev_id}')