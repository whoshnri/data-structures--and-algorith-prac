def lSearch(lists , target):
   for i in range(len(lists)):
    if lists[i]: #checking if the length is valid
        if i == target:
            return f"Target found at index position {lists.index(i)}"
        else:
            continue
    else:
        return "NIL : Target not found in this list"

def verify():
    l = [i for i in range(1 ,201)]
    num = int(input("Enter a number: "))
    print(lSearch(l, num))

verify()