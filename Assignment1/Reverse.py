class Rotate:
    """Without using built in functions rotate the items in an array
    based on the number of steps provided. If steps is > 0 shift items
    to the right. If steps is < 0 shift items to the left. """
    def rotate(self, arr, steps):
        if steps < 0:
            return self.rotate_left(arr, abs(steps))
        else:
            return self.rotate_right(arr, steps)

    def rotate_right(self, arr, steps):
        output = []
        while steps > len(arr):
            steps -= len(arr)
        for i in range(len(arr) - steps, len(arr)):
            output.append(arr[i])
        if len(output) != len(arr):
            for i in range(0, len(arr) - steps):
                output.append(arr[i])
        return output

    def rotate_left(self, arr, steps):
        output = []
        while steps > len(arr):
            steps -= len(arr)
        for i in range(steps, len(arr)):
            output.append(arr[i])
        if len(output) != len(arr):
            for i in range(0, steps):
                output.append(arr[i])
        return output
