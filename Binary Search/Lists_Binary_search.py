#Binary Search programming by Roel Barrera
#lets create an list with random numbers I have typed 
from ctypes.wintypes import tagRECT


array = [1,4,2,5,3,6,7,10,11,11,100,102,101,3]

#Binary search is one of the most useful algorthims that allow us to traverse a list and check for a target
#lets create a target to look in the list for.
target = 11

for x in array:
    if target == x:
        print("We do have ",target)
        break
        #if want it to print all the occurrences comment out the break

#of course we could always do a contains.

print("This is using contains method...")
print("Does the target exist in the list?",array.__contains__(target))