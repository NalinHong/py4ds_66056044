def calculateSum(input):
    count = 0
    for i in input:
        count = count + i

    return count


def calculateProduct(input):
    count = 1
    for i in input:
        count = count * i

    return count


def average(input):
    count = 0
    for i in input:
        count = count + i

    return count / len(input)


def median(input):
    input_sort = input
    input_sort.sort()
    input_len = len(input)
    if input_len == 0:
        return None
    elif input_len % 2 == 0:
        index = input_len // 2
        return (input_sort[index] + input_sort[index - 1]) / 2
    else:
        index = input_len // 2
        return input_sort[index]


def mode(input):  # return first most frequently in a list of numbers
    input_len = len(input)
    count = 0
    if input_len == 0:
        return None
    max_count = 0
    element_having_max_freq = 0
    for i in range(0, input_len):
        count = 0
        for j in range(0, input_len):
            if input[i] == input[j]:
                count += 1
        if count > max_count:
            max_count = count
            element_having_max_freq = input[i]

    return element_having_max_freq


if __name__ == '__main__':
    # calculateSum
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateSum([1, 3, 5, 7, 9]) == 25)

    # calculateProduct
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)

    # average
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)

    # median
    print(median([]) is None)  # Comparison with None performed with equality operators
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)

    # mode
    print(mode([]) is None)  # Comparison with None performed with equality operators
    print(mode([1, 2, 3, 4, 4]) == 4)
    print(mode([1, 1, 2, 3, 4]) == 1)

# %%