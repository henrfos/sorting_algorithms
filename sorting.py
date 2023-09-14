# selection sort


def selection_sort(l):

    for i in range(len(l)-1):
        min_index = i
        for j in range(i+1, len(l)-1):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
    return l


numbers = [1001, 1030, 1050, 1020, 300, 1080, 1100]

s_sort = selection_sort(numbers)

print(s_sort)

# bubble sort


def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list


nums = [210, 15, 111, 90, 45, 120, 150, 200, 100, 140]

b_sort = bubble_sort(nums)
print(b_sort)


# rem dump

def sort_and_rem_dump(a_list):

    new_list = []

    for i in range(len(a_list)-1):
        min_index = i
        for j in range(i+1, len(a_list)-1):
            if a_list[j] < a_list[min_index]:
                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

    for i in a_list:
        if i not in new_list:
            new_list.append(i)
    return new_list


my_list = [5, 4, 3, 2, 1, 2, 3, 4, 5]
n_list = sort_and_rem_dump(my_list)
print(n_list)





