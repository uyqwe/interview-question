#iterative_merge_sort
#can be done better but great to understand

#Merge_sort
import math

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
    
    n=math.log(len(a))
    ns=1
    while(ns<=n):
        l=0
        h=len(a)
        ans=[]
        while(l<h):
            left=a[l:l+ns]
            right=a[l+ns:l+ns+ns]
            #print("left,right=",left,right)
            temp=Merge(left,right)
            #print("temp=",temp)
            ans=ans+temp
            #print("ans=",ans)
            l=l+ns+ns
        a=ans
        ns+=1
    return a
print(Merge_sort(a))
