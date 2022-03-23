class FizzBuzz:
    def fizz_buzz(self, arr):
        output = []
        for i in range(0,len(arr)):
            if arr[i] % 3 ==0 and  arr[i] % 5 == 0:
                output.append("fizzbuzz")
            elif arr[i] % 3 == 0:
                output.append("fizz")
            elif arr[i] % 5 == 0:
                output.append("buzz")
            else:
                output.append(arr[i])
        return output
