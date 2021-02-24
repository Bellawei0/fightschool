

# 636. Exclusive Time of Functions
# https://leetcode.com/problems/exclusive-time-of-functions/



class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res,stack,ts = [0]*n,[],0
        for log in logs:
            pts, pid = ts, stack[-1] if stack else 0
            id,event,ts=log.split(':')
            id,ts = int(id), int(ts)
            if event =='end':
                stack.pop()
                ts+=1
            else:
                stack.append(id)
            res[pid] += ts -pts
            
        return res

#Time complexity : O(n)O(n). We iterate over the entire logslogs array just once. Here, nn refers to the number of elements in the logslogs list.

#Space complexity : The stackstack can grow upto a depth of atmost n/2n/2. Here, nn refers to the number of elements in the given logslogs list.


                
            
            
        
        