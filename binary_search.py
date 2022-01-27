#notes:
#binary search eliminates half the numbers in each step
#logs are the flips of exponentials. How many 10s to multipy to get 100? 2. 10x10=100. log10 100=2.
#binary search only works when your list is in sorted order. ex. phone book in alphabetical order. 

# low = 0
# high = len(list) -1 

# mid = (low + high) / 2
# guess = list[mid]

# if guess < item:
#     low = mid + 1
    
def binary_search(list,item):
    low = 0
    high = len(list)-1      #low and high keep track of which part of the list is being searched
    
    while low <= high:      #while you haven't narrowed it down to one element...
        mid = (low + high)  #check middle element
        guess = list[mid]
        if guess == item:
            return mid      #found the item
        if guess > item:    #guess was too high
            high = mid - 1
        else:               #guess was too low
            low = mid + 1
    return None             #the item doesn't exist

my_list = [1,3,5,7,9]       #test

print(binary_search(my_list, 3)) #returns 1 for index of 1

print(binary_search(my_list, -1)) #returns None

# sorted list of 128 names, what's the maximum number of steps?
# 128 / 2 = 64
# 64 / 2 = 32
# 32 / 2 = 16
# 16 / 2 = 8
# 8 / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# seven steps #doubling 128 would only make it eight steps. 

# O(n) is linear time for a simple search. O(log n) is logarithmic time, or log time for binary search.
#five most common run times are O(log n), O(n), O(n log n), O(n2), O(n!)
            
    
    