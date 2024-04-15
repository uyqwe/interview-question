#Google interview Question: 
'''
Question - There's an input stream where you receive messages from another system. 
The frequency of messages is pretty high such that your system would not handle such huge amount of message processing.

Task to achieve - Duplicate messages should be completely removed from the output if they occur within 10 seconds.
'''

# input 
arr=[(10,'A'),(12,'B'), (13,'C'), (14,'A'), (17, 'B'), (23, 'A'), (35, 'A')]

#Output
#arr=[(10,'A'),(12,'B'), (13,'C'),(35, 'A')]

def duplicate_remove(arr):
    dic={}
    lat={}
    ans=[]
    for time, msg in arr:
        if msg not in dic:
            dic[msg]= [time]
            lat[msg]= time
        else:
            if abs(time-lat[msg])<10:
                lat[msg]=time
                continue
            else:
                dic[msg].append(time)
    #print(dic)
    for key in dic:
        for i in dic[key]:
            ans.append((i,key))
    ans.sort()
    #print(ans)
    return ans
    
        


ans=duplicate_remove(arr)
print(ans)
