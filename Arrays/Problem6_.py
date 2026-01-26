class Problem6_:
    def rightRotateArray(self, arr, k):
        n = len(arr)

        k = k % n
        arr[n - k:] = reversed(arr[n - k:])
        arr[:n - k] = reversed(arr[:n - k])
        arr[:] = reversed(arr)

        return arr

obj = Problem6_()
arr = [1,2,3,4,5,6,7,8,9]
print(obj.rightRotateArray(arr,6))