# @arg arr The input arr like object to be sorted
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
    temp = []
    i = 0
    n = 0
    while i < len(arr) and n < len(cmp):
        if arr[i] < cmp[n]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(cmp[n])
            n += 1
    if i == len(arr):
        temp.extend(cmp[n:])
    else:
        temp.extend(arr[i:])
    l = temp
    return l

#my test harness

#arr = input("Please enter an array: ")
#cmp = input("Please enter an array: ")
#temp = merge_sort(arr,cmp)
#temp.sort()
#print(temp)

##############################################################################
############################ QUICK SORT FUNCTION #############################
##############################################################################

def quick_sort(arr, cmp):
    if arr == cmp:
        sorted = arr
        return sorted
    if arr == []:  
        return []
    pivot = arr[0]
    l = quick_sort([x for x in arr[1:] if x < pivot])
    u = quick_sort([x for x in arr[1:] if x >= pivot])
    sorted = l + [pivot] + u
    return sorted