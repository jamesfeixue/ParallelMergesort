"""
James Xue
Heterogenous Processing
Homework 3

Implementing the Merge Sort Algorithm.


"""


class MergeSort:

    """

    Serial Implementation of Merge Sort

    """
    def merge_sort_serial(self, a_cpu):
        # a_cpu: an array generated in cpu.
        # return: the sorted array of a_cpu.
        a_length = len(a_cpu)

        #Base case
        if a_length <= 1:
            return a_cpu

        #Recursive Case
        a_mid = int(a_length/2)
        left = a_cpu[ 0 : a_mid]
        right = a_cpu[ a_mid : len(a_cpu)]

        #Recursively Sort
        merge_sort = MergeSort()
        left = merge_sort.merge_sort_serial(left)
        right = merge_sort.merge_sort_serial(right)

        return merge_sort.merge_serial(left, right)

    def merge_serial(self, left_cpu, right_cpu):
        #initialize
        result = []

        # while not empty
        while (len(left_cpu)>0 and len(right_cpu)>0):
            left_first = left_cpu[0]
            right_first = right_cpu[0]
            # print(left_first, type(left_first), right_first, type(right_first))
            if (left_first <= right_first):
                result.append(left_cpu[0])
                left_cpu = left_cpu[1:len(left_cpu)]
            else:
                result.append(right_cpu[0])
                right_cpu = right_cpu[1:len(right_cpu)]

        # consume other when one is empty
        if len(left_cpu) == 0:
            result = result + right_cpu
        elif len(right_cpu) == 0:
            result = result + left_cpu
        else:
            print("length error")

        print(result)
        return result

    """
    
    Parallel Implementations of Merge Sort
    
    """
    def merge_sort_naive(self, a_cpu):
        # a_cpu: an array generated in cpu.
        # return: the sorted array of a_cpu.
    def merge_sort_optimized1(self, a_cpu):
        # a_cpu: an array generated in cpu.
        # return: the sorted array of a_cpu.
    def merge_sort_optimized2(self, a_cpu):
        # a_cpu: an array generated in cpu.
        # return: the sorted array of a_cpu.

#%%
ms = MergeSort()
result = ms.merge_sort_serial([1, 2, 3, 5, 6, 9, 1, 2, 3, 4])
print (result)