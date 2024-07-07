class Solution:
    def maximumProduct(self,nums:list[int])->int:
        nums.sort()
        return max(nums[-1]*nums[0]*nums[1],nums[-1]*nums[-2]*nums[-3])
sol=Solution()
list=[3,5,6,7,2]
result=sol.maximumProduct(list)    
print(result)