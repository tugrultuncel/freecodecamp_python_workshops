# ''' list practices i've done
# '''
# list1 = [0,1,2,3,4,5,6,7,8,9]
# key = 'qwerty'
# key1 = list(key)


# print(list1[0])
# print(key1)


# list1.append(key1[0])
# print(list1)

# ### PRINTS
# # list[0]
# # ['q', 'w', 'e', 'r', 't', 'y']
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'q']

# print(list1[1:4])
# list1 = [0,1,2,3,4,5,6,7,8,9]
# list1.append(key1[0:3])
# print(list1)

# ### PRINTS
# #[1, 2, 3]
# #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ['q', 'w', 'e']]

# list1 = [0,1,2,3,4,5,6,7,8,9]
# list1.extend(key1[0:3])
# # list1=str(list1[10])
# print(list1)

# ## PRINTS

# # 0
# # ['q', 'w', 'e', 'r', 't', 'y']
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'q']
# # [1, 2, 3]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, ['q', 'w', 'e']]
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'q', 'w', 'e']

a1=[1,2,3,4,5]
# a2=['a','s','d','f']
print(f'a1 = {a1}')
# print(a2)
a1.insert(5,6)
print(f'a1.insert (5,6) = {a1}')
a1.remove(6)
print(f'a1.remove(6) = {a1}')
print(f'a1.index(1) = {a1.index(1)}')
a3='list'
list(a3)
print(a3)
print(list(a3))
print(tuple(a3))

## UNPACKING

i0, i1, i2, i3, i4 = a1
print(i0)
print(i4)

i0, i1, i2, *i3 = a1
print(i0)
print(i4)
print(i3)
print(list(i3))
print(list(i3))
print(*i3)
programming_languages = ('Rust', 'Java', 'Python', 'C++', 'Rust', 'Python', 'JavaScript', 'Python')
print(programming_languages.index('Python', 3, 7))
print(sorted(programming_languages))
# print(programming_languages.sort())
