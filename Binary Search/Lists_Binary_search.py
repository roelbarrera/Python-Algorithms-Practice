#Binary Search programming by Roel Barrera
#lets create an list with random numbers I have typed 

#function for advance binarysearch
def binsearchsorted(array, low, high, target):
    #basecase for rescursion
    if high >= low:
        
        #// to divide and return a whole number
        mid = (high + low) // 2

        #now that we have a middle number lets check if that is the target number
        if array[mid] == target:
            return mid
        

        #if the element is smaller than the mid, if it is in there its in the left
        #so we call the function again but with the new high which will be middle -1
        if array[mid] > target:
            return binsearchsorted(array, low, mid - 1, target)

        #if the above condition is not met, if its present is must be on the right
        #so we call the function again but with a new low which will be the middle +1
        else:
            return binsearchsorted(array, mid + 1, high, target)



    #if this condition is met it means the element is not in the array
    #the function should have already called it self enough to either reach it
    #or its not there
    else:

        return -1


array = [1,4,2,5,3,6,7,10,11,11,100,102,101,3]

#Binary search is one of the most useful algorthims that allow us to traverse a list and check for a target
#lets create a target to look in the list for.
target = 100

for x in array:
    if target == x:
        print("We do have ",target)
        break
        #if want it to print all the occurrences comment out the break

#of course we could always do a contains.

print("This is using contains method...")
print("Does the target exist in the list?",array.__contains__(target))

#How do we make this faster? We can sort and using the divide and conquer approach.
#for the purposes of this example we will be using the built in sort method.
array.sort()

print("Here is the list that is already sorted: ",array)


#in order to use the divide and conquer approach we need to first create a start point, a middle point, and a end point.
#lets send this to a function and use recursion
low = 0
high = (array.__len__() - 1)

result = binsearchsorted(array, low, high, target)
 
if result != -1:
    print("Target is present at index", str(result))

else:
    print("Target is not present in array/list")

