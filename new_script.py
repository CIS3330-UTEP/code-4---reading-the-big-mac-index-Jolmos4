import pandas as pd

# fruits = ['apple','melon','grapes','orange', 'kiwi']
# fruit_series = pd.Series(fruits)

# print('fruits')
# print(fruits)
# print('fruit series')
# print(fruit_series)



# colors = ['orange','white','blue','green']

# print(type(colors))

# colors_series = pd.Series(colors)

# print(type(colors_series))

# print(colors_series)



students = {"Kansas": "Yvan", "New Mexico": "Abdel", "Wisconsin": "Jon", "Tennesee": "Andrew"}

print(type(students))

print(students.values())
print(students.keys())

students_series = pd.Series(data=students.values(),index=students.keys())





