def count_sublists(numbers):  
    sum = 1
    result = 1

    for i in range(1, len(numbers)):
        if numbers[i - 1] < numbers[i]:
            sum += 1
        else:
            sum = 1
        result += sum

    return result

if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4])) # 7
    print(count_sublists([1, 2, 3, 4])) # 10
    print(count_sublists([4, 3, 2, 1])) # 4
    print(count_sublists([1, 1, 1, 1])) # 4
    print(count_sublists([1, 2, 1, 2])) # 6

    numbers = list(range(1, 10**5+1))
    print(count_sublists(numbers)) # 5000050000

