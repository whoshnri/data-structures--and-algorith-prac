#python lists are arrays in other languages.
#but the applications and operations are those of arrays

#creating a new list(array)
new_list = [1,2,3,4,5,6,7,8,9,10] # these values arent stored directly, but the addresses are stored an it references the values that are else where

#accessing the array
print(new_list[2])

#searching through an array
#using the iterable "in" -- this is a linear search methid prebuilt for thelist type
target = 1

print(True if target in new_list else False)


#using the for loop to perform comparison

for i in new_list:
    if i == target:
        print(True)
        break


#inserting 
#direct inserting 
new_list.insert(0, 0) #the first parameter is the index where the insertion is to happen
# print(new_list)

#appending to the end of the list
new_list.append(55)
# print(new_list)

#extending a list - inserting a list by another list
#M1>>
new_list.extend([56,57,58])
# print(new_list)

#M2
extension = [59 ,60]
new_list.extend(extension) 
print(new_list)