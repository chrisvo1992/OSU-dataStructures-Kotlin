**Problem 1 - Min Max**
Write a function that receives a one dimensional array of integers and returns a Python
tuple with two values - minimum and maximum values in the input array. You may assume
that the input array will contain only integers and will have at least one element. You do not
need to check for those conditions.

**Problem 2 - Fizz Buzz**
Write a function that receives a StaticArray with integers and returns a new StaticArray
object with the content from the original array, modified as follows:
1) If the number in the original array is divisible by 3, the corresponding element in the
new array should be a string ‘fizz’.
2) If the number in the original array is divisible by 5, the corresponding element in the
new array should be a string ‘buzz’.
3) If the number in the original array is both a multiple of 3 and a multiple of 5, the
corresponding element in the new array should be a string ‘fizzbuzz’.
4) If all other cases, the element in the new array should have the same value as in the
original array.
Content of the input array should not be changed. You may assume that the input array will
contain only integers and will have at least one element. You do not need to check for those
conditions.

**Problem 3 - Reverse**
Write a function that receives a StaticArray and reverses the order of the elements in the
array. Reversal must be done ‘in place’, meaning the original input array will be modified.
You may assume that the input array will contain at least one element.

**Problem 4 - Rotate**
Write a function that receives two parameters - a StaticArray and an integer value (called
steps ). The function will create and return a new StaticArray where all elements are from
the original array but their position has shifted right or left steps number of times. Original
array should not be modified.
If steps is a positive integer, elements should be rotated right. Otherwise, rotation is to the
left. Please see code examples below for the additional details. You may assume that the
input array will have at least one element.

**Problem 5 - Range**
Write a function that receives two integers start and end and returns a StaticArray that
contains consecutive values that begin at start and end at end (inclusive).

**Problem 6 - Is Sorted?**
Write a function that receives a StaticArray and returns an integer that describes whether
the array is sorted. Method should return 1 if the array is sorted in strictly ascending order.
It should return 2 if the list is sorted in strictly descending order. Otherwise the method
should return 0. Arrays consisting of a single element are considered sorted in strictly
ascending order.
When implementing this method, you may assume that values stored in the array are all of
the same type (either all numbers, or strings, or custom objects, but never a mix of those).
You do not need to write checks for this condition.

**Problem 7 - Sort**
Write a function that receives a StaticArray and sorts its content in non-descending order.
Sorting must be done ‘in place’, meaning the original input array will be modified.
You may assume that the input array will contain at least one element and that values
stored in the array are all of the same type (either all numbers, or strings, or custom
objects, but never a mix of those). You do not need to write checks for these conditions.
You can implement any sort method of your choice. Sorting does not have to be very
efficient or fast, a simple insertion or bubble sort will suffice. Duplicates in the original array
can be placed in any relative order in the sorted array (in other words, your sort does not
have to be ‘stable’).

**Problem 8 - Remove Duplicates**
Write a function that receives a StaticArray where the elements are already in sorted order
and returns a new StaticArray with duplicate values removed. Original array should not be
modified.
You may assume that the input array will contain at least one element, values stored in the
array are all of the same type (either all numbers, or strings, or custom objects, but never a
mix of those) and that elements of the input array already are in the sorted order. You do
not need to write checks for these conditions.
