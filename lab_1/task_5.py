inArray = ['a', ['c', 1, 3], ['f', 7, [4, '4']], [{'lalala': 111}]]
array = []


def do(arr):
    for i in arr:
        if isinstance(i, list) or isinstance(i, tuple):
            do(i)
        else:
            array.append(i)
    return


do(inArray)

print("array: ", array)
