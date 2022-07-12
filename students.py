# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

###

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")

# for student in students:
#     print(student)

###

import csv
from turtle import home

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})
    #reader = csv.reader(file) #в файле students.csv есть разные строки, чтобы их распознать
    # исп-ся модуль csv, в частности его функция reader для определения и чтения строк
    #for name, home in reader: # тут reader определил по два знач-я на строку
                              # и к каждому присваевает переменные name и home 
        #students.append({"name": name, "home": home})

for student in sorted(students, key = lambda student: student["name"]): #после ключа, 
    # идет анонимная функция с рандомным названием стюдент , которая запрашивает 
    # со словаря стюдент имя, вызываемое в своей очереди ключом нэйм
    print (f"{student['name']} is  {student['home']}")