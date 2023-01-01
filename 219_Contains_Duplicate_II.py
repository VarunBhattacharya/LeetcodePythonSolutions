class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i]  in hashMap and i - hashMap[nums[i]] <= k:
                return True
            hashMap[nums[i]] = i
        return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    k = 3
    print(Solution().containsNearbyDuplicate(nums, k))