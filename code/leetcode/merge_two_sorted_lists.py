from typing import List
def mergeTwoSorteList(l1, l2):
    print(l1, l2)
    l1.extend(l2)
    numbers = l1
    len_numbers = len(l1)
    for i in range(len_numbers):
        for j in range(len_numbers -1 - i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]    
    return numbers
    
if __name__ == '__main__':
    l1 = [1,2,4]
    l2 = [1,3,4]
    print(mergeTwoSorteList(l1, l2))