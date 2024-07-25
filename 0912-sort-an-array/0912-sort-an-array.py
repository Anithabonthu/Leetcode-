class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def mergeSort(arr,left,right):
            if left>=right:
                return
            mid=(left+right)//2
            mergeSort(arr,left,mid)
            mergeSort(arr,mid+1,right)
            merge(arr,left,mid,right)
        def merge(arr,left,mid,right):
            n1=mid-left+1
            n2=right-mid
            leftArray=nums[left:mid+1]
            rightArray=nums[mid+1:right+1]
            i=j=0
            k=left
            while(i<n1 and j<n2):
                if leftArray[i]<=rightArray[j]:
                    nums[k]=leftArray[i]
                    i+=1
                else:
                    nums[k]=rightArray[j]
                    j+=1
                k+=1
            while i<n1:
                nums[k]=leftArray[i]
                i+=1
                k+=1
            while j<n2:
                nums[k]=rightArray[j]
                j+=1
                k+=1
        mergeSort(nums,0,len(nums)-1)
        return nums

