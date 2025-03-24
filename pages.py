from itertools import groupby

def create_string(pages):
    pages = sorted(set(pages))
    r = []

    def f(a, b):
        return str(a) if a == b else f"{a}-{b}"

    for k, g in groupby(enumerate(pages), lambda x: x[0] - x[1]):
        group = list(g)
        r.append(f(group[0][1], group[-1][1]))

    return ",".join(r)

if __name__ == "__main__":
    print(create_string([1]))  # "1"
    print(create_string([1, 2, 3]))  # "1-3"
    print(create_string([1, 1, 1]))  # "1"
    print(create_string([1, 2, 1, 2]))  # "1-2"
    print(create_string([1, 6, 2, 5]))  # "1-2,5-6"
    print(create_string([1, 3, 5, 7]))  # "1,3,5,7"
    print(create_string([1, 8, 2, 7, 3, 6, 4, 5]))  # "1-8"
    print(create_string([3, 2, 9, 4, 3, 6, 9, 8]))  # "2-4,6,8-9"

    pages = [3, 2, 1, 3, 2, 1]
    print(create_string(pages))  # "1-3"
    print(pages)  # [3, 2, 1, 3, 2, 1]