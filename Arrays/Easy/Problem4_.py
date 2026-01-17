class Problem4_:
    def removeDuplicate(self, arr):
        n = len(arr)
        if(n == 1):
            return 1
        
        i = 0 
        j = i+1
        while j<n:
            if arr[j] != arr[i]:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
            j+=1
        return i+1
    
obj = Problem4_()
arr = [0,0,1,1,1,2,2,3,3,4]
print(obj.removeDuplicate(arr))