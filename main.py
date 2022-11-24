# @arg arr The input list like object to be sorted
# @arg cmp A compare function which takes two element in the array, 
#          cmp(a,b)<0   if a should be placed before b,
#          cmp(a,b)==0  if arr is still sorted after a and b are exchanged,
#          cmp(a,b)>0   if a should be placed behind b.
def multi_sort(arr, cmp, method="None"):
    if(method=="quick"):
        quick_sort(arr,cmp)
    elif(method=="merge"):
        merge_sort(arr,cmp)
    elif(method=="None"): # do nothing
        return
    else:
        print("invalid argument!")


##############################################################################
############################ MERGE SORT FUNCTION #############################
##############################################################################


def merge_sort(arr,cmp):
    l3 = []
    i = 0
    n = 0
    while i < len(arr) and n < len(cmp):
        if arr[i] < cmp[n]:
            l3.append(arr[i])
            i += 1
        else:
            l3.append(cmp[n])
            n += 1
    if i == len(arr):
        l3.extend(cmp[n:])
    else:
        l3.extend(arr[i:])
    l = l3
    return l

#my test harness

#arr = input("Please enter an array: ")
#cmp = input("Please enter an array: ")
#l3 = merge_sort(arr,cmp)
#l3.sort()
#print(l3)

##############################################################################
############################ QUICK SORT FUNCTION #############################
##############################################################################

# must be in-place sort
def quick_sort(arr,cmp):
    pass