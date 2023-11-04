def task_1():
    user_input = str(input("Input: ")).lower()
    lists = []
    for char in user_input:
        lists.append(char)
    print(lists)


# task_1()
def task_2():
    user_input = "Pulp Fiction".lower()
    lists = []
    for char in user_input:
        count = user_input.count(char)
        if (char, count) not in lists:
            lists.append((char, count))
    print(lists)


# task_2()

def task_3():
    user_input = "Pulp Fiction".lower()
    lists = []
    vow_lists = []
    list_vow = []
    list_cons = []
    list_sym = []

    for letter in ('aeiouy'):
        vow_lists.append(letter)

    for char in user_input:
        count = user_input.count(char)
        if (char, count) not in lists:
            lists.append((char, count))

    for element, count in lists:
        if element == ' ':
            list_sym.append((element, count))
        elif element not in vow_lists:
            list_cons.append((element, count))
        else:
            list_vow.append((element, count))

    print(f"{list_vow}\n{list_cons}\n{list_sym}")


# task_3()

def task_4():
    user_input = input("Input: ").replace(" ", "").split(',')
    list_number = []
    for number in user_input:
        number = int(number)
        list_number.append(number)

    len_list = len(list_number) // 4
    list_number.sort()

    q1, q2, q3, q4 = [], [], [], []

    for x in list_number:
        index = list_number.index(x)
        if len(q1) < len_list:
            q1.append(x)
        elif len(q2) < len_list:
            q2.append(x)
        elif len(q3) < len_list:
            q3.append(x)
        elif len(q4) < len_list:
            q4.append(x)
    print(f"{q1}\n{q2}\n{q3}\n{q4}")


# task_4()

def task2_1():
    user_name = str(input("Name: ")).replace(" ", "").split(',')
    user_assignments = input("Assignments: ").replace(" ", "").split(',')
    user_labs = input("Labs: ").replace(" ", "").split(',')
    user_test = input("Test: ").replace(" ", "").split(',')

    dict_user = {"name": user_name, "assignments": user_assignments, "labs": user_labs, "test": user_test}

    print(dict_user)


# task2_1()

def task2_2():
    user_name = str(input("Name: ")).replace(" ", "").split(',')
    user_assignments = input("Assignments: ").replace(" ", "").split(',')
    user_labs = input("Labs: ").replace(" ", "").split(',')
    user_test = input("Test: ").replace(" ", "").split(',')

    dict_user = {}

    dict_user["name"] = user_name
    dict_user["assignments"] = user_assignments
    dict_user["labs"] = user_labs
    dict_user["test"] = user_test

    len_dict = len(dict_user["labs"]) + len(dict_user["assignments"])

    print(len_dict)


# task2_2()

def task2_3():
    user_name = str(input("Name: ")).replace(" ", "").split(',')
    user_assignments = input("Assignments: ").replace(" ", "").split(',')
    user_labs = input("Labs: ").replace(" ", "").split(',')
    user_test = input("Test: ").replace(" ", "").split(',')

    dict_user = {}

    dict_user["name"] = user_name
    dict_user["assignments"] = [int(x) for x in user_assignments]
    dict_user["labs"] = [int(x) for x in user_labs]
    dict_user["test"] = [int(x) for x in user_test]

    def result(assignments, labs, test):
        return (sum(assignments) / 2 * 0.3) + (sum(labs) / 2 * 0.5) + (sum(test) / 2 * 0.2)

    print(result(dict_user["assignments"], dict_user["labs"], dict_user["test"]))


# task2_3()

def task2_4():
    dict_user1 = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2],
                  'final_grade': 70.25}
    dict_user2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}

    students = {dict_user1["name"]: {k: v for k, v in dict_user1.items() if k != 'name'},
                dict_user2['name']: {k: v for k, v in dict_user2.items() if k != 'name'}}

    print(students)


# task2_4()


def task3():
    # Нужно добавить mft
    lists = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2),
             (1001, 1)]

    # Здесь в целом не нужно быстрая сортировка (алгоритм), но так как я уже это сделал не хочется удалить
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[0]
        less = [x for x in arr[1:] if x[0] < pivot[0]]
        equal = [x for x in arr[1:] if x[0] == pivot[0]]
        greater = [x for x in arr[1:] if x[0] > pivot[0]]

        return quick_sort(less) + equal + [pivot] + quick_sort(greater)

    new_sorted_list = quick_sort(lists)

    dauletsuper = {}

    for i in new_sorted_list:
        name = i[0]
        find_element = i[-1]

        count = new_sorted_list.count(i)

        if i[0] not in dauletsuper:
            dauletsuper[name] = {find_element: count, 'mft': find_element, 'lft': find_element}

        else:
            if find_element not in dauletsuper[name]:
                dauletsuper[name][find_element] = count
            else:
                dauletsuper[name][find_element] += count

        if count > dauletsuper[name][dauletsuper[name]['mft']]:
            dauletsuper[name]['mft'] = find_element

        if count < dauletsuper[name][dauletsuper[name]['lft']]:
            dauletsuper[name]['lft'] = find_element

    print(dauletsuper)


# task3()


a= {
    "name": "Daulet",
    "labs": [76.5, 76, 100]
}
labs = a['labs'][2]
print()