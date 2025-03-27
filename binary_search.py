#intro to algorithm course
#binary search algorithm

def binary_search(l , target):
    first = 0
    last = len(l) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if l[first] == target:
            return first
        elif l[last] == target:
            return last
        else:
            if l[midpoint] == target:
                return midpoint
            else:
                if l[midpoint] < target:
                    first = midpoint - 1
                else: 
                    last = midpoint + 1
    return None

def verify():
    arr = [i for i in range(1 , 201)]
    num = int(input("Enter a number: "))
    print(f"Number found at index position {binary_search(arr , num)}")

verify()