class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
    
# Time complexity O(n)
# Space complexity O(1)


'''
# Visualization

Here's how the matrix changes by always extracting the first row and rotating the remaining matrix counter-clockwise:

    |1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
    |4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
    |7 8 9|      |4 7|
Now look at the first rows we extracted:

    |1 2 3|      |6 9|      |8 7|      |4|      |5|
Those concatenated are the desired result.


# Another visualization
  spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]

'''