class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=len(nums)-1
#firstapproach brute
        '''for i in range(0,len(nums)):
            if nums[i]==0:
                zero+=1
            if nums[i]==1:
                one+=1
            if nums[i]==2:
                two+=1
        #print(zero,one,two)
        ind=0
        while(zero!=0):
            nums[ind]=0
            zero-=1
            ind+=1
        #print(ind)
        while(one!=0):
            nums[ind]=1
            one-=1
            ind+=1
        #print(ind)
        while(two!=0):
            nums[ind]=2
            two-=1
            if ind==len(nums)-1:
                break
            ind+=1'''
#second approach
        n=len(nums)-1        
        two=n
        curr=0
        while(curr<=two):
            if nums[curr]==0:
                nums[curr], nums[one] = nums[one], nums[curr]
                one+=1
                curr+=1
                continue
            if nums[curr]==1:
                curr+=1
                continue
            if nums[curr]==2:
                nums[curr], nums[two] = nums[two], nums[curr]   
                two-=1 
                continue

        

        

        
