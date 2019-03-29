def bubble_sort(obj_list):

        for obj in range(len(obj_list)):
            for i in range(len(obj_list) - 1):
                if obj_list[i].compare (obj_list[i + 1]) > 0:
                    obj_list[i], obj_list[i + 1] = obj_list[i + 1], obj_list[i]


def binary_search(obj_list, obj):

    return binarySearch(obj_list, 0, len(obj_list)-1, obj)


def binarySearch(obj_list, left, right, obj):

    if right >= left:

        middle = (left + right) // 2

        if obj_list[middle].compare(obj)== 0:

            return middle

        if obj_list[middle].compare(obj) > 0:

            return binarySearch(obj_list, left, middle -1, obj)

        else:
            return binarySearch(obj_list, middle +1, right, obj)

    else:
        return -1


def linear_search(obj_list, obj):

        for i in range(len(obj_list)):
            if obj_list[i].compare(obj) == 0:
                return 1

        return -1
