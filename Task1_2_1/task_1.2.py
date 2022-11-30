import re
pattern = r"\w+\.\d+"
ides = re.compile(pattern)

def log(filename):
    file = open(filename, "r")
    file_lines = file.readlines()
    file.close()
    list = []

    count = 0

    for line in file_lines:
        if 'D:TUpdaterController::SetUniqueParam(429): eid:' in line:
            list.append(line)

            count += 1

    return list

def two_eids(list):

    prelast = list[-2]
    last = list[-1]

    list_prelast = re.findall(pattern, prelast)
    list_last = re.findall(pattern, last)

    first_dict = dict(item.split('.') for item in list_prelast)
    second_dict = dict(item.split('.') for item in list_last)

    value = set(first_dict.items()) ^ set(second_dict.items())

    return value

if __name__ == "__main__":
    result = log("Log.txt")
    print("Предпоследний лог \n", result[-2])
    print("Последний лог \n", result[-1])
    print("Отличие в логах \n", two_eids(result))






