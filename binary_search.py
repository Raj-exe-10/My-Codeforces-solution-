def binary_search(arr,low,high,item):
    if low<=high:
        mid = (low + high) // 2
        if arr[mid]==item:
            return mid
        elif arr[mid]>item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)
    else:
        return -1

l=[10,20,30,40,50,60,70,80,90,100,110]
print(binary_search(l,0,10,120))

