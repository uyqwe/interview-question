#Merge_sort

a=[2,1,4,3,5,8,7,6]

def Merge(left,right):
    pa=0
    pb=0
    ls=[]
    while(pa<len(left) and pb<len(right)):
        if left[pa]<right[pb]:
            ls.append(left[pa])
            pa+=1 
        else:
            ls.append(right[pb])
            pb+=1 
    while(pa<len(left)):
        ls.append(left[pa])
        pa+=1 
    while(pb<len(right)):
        ls.append(right[pb])
        pb+=1 
        
    return ls
    
    
def Merge_sort(a):
    if len(a)<2:
        return a
    mid=(len(a)//2)
    left=Merge_sort(a[:mid])
    right=Merge_sort(a[mid:])
    return Merge(left,right)
print(Merge_sort(a))
