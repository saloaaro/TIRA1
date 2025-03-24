def create_distribution(string):
    n = len(string)
    s = set()

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = string[i:j]
            s.add(sub)

    d = {}
    for k in range(1, n + 1):
        d[k] = 0

    for sub in s:
        d[len(sub)] += 1

    return d

if __name__ == "__main__":
    print(create_distribution("aaaa")) 
    # {1: 1, 2: 1, 3: 1, 4: 1}

    print(create_distribution("abab")) 
    # {1: 2, 2: 2, 3: 2, 4: 1}

    print(create_distribution("abcd")) 
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb")) 
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu")) 
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
