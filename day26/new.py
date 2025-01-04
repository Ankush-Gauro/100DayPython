import random
import pandas as pd

li = [1,2,3]
new_li = [x+1 for x in li]
print(new_li)

new_li = [x*2 for x in range(1,5)]
print(new_li)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
scores = {x:random.randint(1,100) for x in names}
print(scores)

students = {'students': names,
            'marks': [random.randint(1,100) for x in names]}

passed_students = {x:y for (x,y) in scores.items() if y > 50}
print(passed_students)  

for (student, score) in scores.items():
    print(student)

for (student, score) in scores.items():
    print(score)

data = pd.DataFrame(students)
print(data)

for (student, score) in data.items():
    print(student)
print('\n\n\n\n')
for (student, score) in data.items():
    print(score)

for (index, row) in data.iterrows():
    print(row.students)


for (index, row) in data.iterrows():
    print(row.marks)

for (index, row) in data.iterrows():
    if row.marks > 50:
        print(row.students)
