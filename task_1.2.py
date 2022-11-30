import re

file = open("Log.txt", "r")
file_lines = file.readlines()
file.close()
list = []
pattern = r"\w+\.\d+"
ides = re.compile(pattern)

#count =0

for i in file_lines:
    if 'D:TUpdaterController::SetUniqueParam(429): eid:' in i:
        list.append(i)

 #       count += 1
list_2eids = list[-2:]

prelast = list_2eids[-2]
last = list_2eids[-1]

#print(count)
print(list)

print("Два последних лога ", list)
print("Предпоследний с ied ", prelast)
print("Последний с eid ", last)


list_prelast = re.findall(pattern, prelast)
list_last = re.findall(pattern, last)

print("Предпоследний лог без ied ", list_prelast)
print("Последний лог без ied ", list_last)

first_dict = dict(x.split('.') for x in list_prelast)
second_dict = dict(y.split('.') for y in list_last)

print(first_dict)
print(second_dict)

value = set(first_dict.items()) ^ set(second_dict.items())

print("Отличие в двух словарях ", value)






