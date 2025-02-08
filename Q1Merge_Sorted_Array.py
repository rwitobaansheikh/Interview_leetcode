class Solution:
    def merge(self, nums1: [], m: int, nums2: [], n: int):
        nums1[m:] = nums2
        nums1.sort()
        return nums1
    
def main():
    nums1=[1,2,3,0,0,0]
    m=3
    nums2=[2,5,6]
    n=3
    s=Solution()
    print(s.merge(nums1,m,nums2,n))
    
if __name__ == "__main__":
    main()