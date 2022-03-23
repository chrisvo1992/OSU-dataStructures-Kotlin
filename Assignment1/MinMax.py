class MinMax:
    def min_max(self, arr):
        min, max = arr[0], arr[0]
        for i in range(1,len(arr)):
            if min > arr[i]:
                min = arr[i]
            elif max < arr[i]:
                max = arr[i]
        return (min,max)
