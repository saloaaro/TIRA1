def count_sublists(numbers):
    sum = 0
    result = 0

    for i in numbers:
        if i % 2 == 0:
            sum += 1
        else:
            sum = 0
        result += sum

    return result

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000
