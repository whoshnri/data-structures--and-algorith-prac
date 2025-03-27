def recursive_binary_search(l, target):
    if len(l) == 0:
        return False
    else:
        midpoint = len(l) // 2
        if l[midpoint] == target:
            return True
        else:
            if l[Gmidpoint] < target:
                return recursive_binary_search(l[midpoint+1:] , target)
            else: 
                return recursive_binary_search(l[:midpoint] , target)

def verify():
    arr = [i for i in range(1 , 201)]
    num = int(input("Enter a number: "))
    print(f"Target found : " , recursive_binary_search(arr , num))

verify()
