import math

class Comparer:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = 0
        n = len(self.numbers)
        self.bound = n * math.floor(math.log2(n))

    def list_size(self):
        return len(self.numbers)

    def smaller(self, a, b):
        self.counter += 1
        if self.counter > self.bound:
            raise RuntimeError("too many comparisons")
        return self.numbers[a] < self.numbers[b]

def find_list(comparer):
    n = comparer.list_size()
    
    # Luodaan lista indekseistä
    indices = list(range(n))
    
    # Funktio, joka järjestää listan vertailujen avulla
    def merge_sort(indices):
        if len(indices) <= 1:
            return indices
        
        mid = len(indices) // 2
        left = merge_sort(indices[:mid])
        right = merge_sort(indices[mid:])
        
        # Yhdistetään vasen ja oikea osa
        result = []
        while left and right:
            if comparer.smaller(left[0], right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        
        result.extend(left)
        result.extend(right)
        
        return result
    
    # Suoritetaan merge sort ja palautetaan järjestetty lista
    sorted_indices = merge_sort(indices)
    
    # Järjestetään alkuperäisen listan arvojen mukaan
    sorted_list = [comparer.numbers[i] for i in sorted_indices]
    
    return sorted_list

# Testit
if __name__ == "__main__":
    comparer = Comparer([3, 1, 2, 4])
    numbers = find_list(comparer)
    print(numbers)  # [3, 1, 2, 4]

    comparer = Comparer([1, 6, 2, 5, 3, 4])
    numbers = find_list(comparer)
    print(numbers)  # [1, 6, 2, 5, 3, 4]
