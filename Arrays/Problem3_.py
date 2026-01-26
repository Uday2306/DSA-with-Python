arr = [1,2,2,3,4,4,5]

class Problem3_:
    def is_sorted(self, arr):
        
        n = len(arr)
        for i in range(1,n):
            if arr[i] >= arr[i-1]:
                {}
            else:
                return False
            
        return True

obj = Problem3_()
print(obj.is_sorted(arr))