class IsSorted:
    """Returns 1 if the given array is in sorted ascending order,
    returns 2 if it is in descending order, or 0 if it is neither.
    These functions do not use built in copy() functions. """
    def is_sorted(self, arr):
        if self.is_ascending(arr):
            return 1
        elif self.is_descending(arr):
            return 2
        else:
            return 0

    def is_ascending(self, arr) -> bool:
        value = arr[0]
        for i in range(1, len(arr)):
            if value <= arr[i]:
                return False
            value = arr[i]

        return True

    def is_descending(self, arr) -> bool:
        value = arr[0]
        for i in range(1, len(arr)):
            if value >= arr[i]:
                return False
            value = arr[i]
        return True
