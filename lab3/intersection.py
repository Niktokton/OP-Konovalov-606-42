# def intersect(list1, list2):  # Без рекурсии
#     return list(set(list1) & set(list2))


def intersect(list1, list2):  # Рекурсия
    if not list1 or not list2:
        return []
    list1 = list(set(list1))
    list2 = list(set(list2))
    tmp = list1[0]
    if tmp in list2:
        return [tmp] + intersect(list1[1:], list2)
    else:
        return intersect(list1[1:], list2)


print(intersect([1, 2, 3, 4], [2, 3, 4, 6, 8]))
print(intersect([5, 8, 2], [2, 9, 1]))
print(intersect([5, 8, 2], [7, 4]))
