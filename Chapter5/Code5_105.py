  import numpy as np
    
    # Calculate element-wise minimum of array elements
    print("\nCalculate the minimum elements between two arrays by means of the np.minimum() function")
    minimum = np.minimum([2, 3, 4], [1, 5, 2])
    print("np.minimum([2, 3, 4], [1, 5, 2]) =", minimum, ", with a dimension of", minimum.ndim)
    # Output: np.minimum([2, 3, 4], [1, 5, 2]) = [1 3 2] , with a dimension of 1
    
    # Calculate element-wise maximum of array elements
    print("\nCalculate the maximum elements between two arrays by means of the np.maximum() function")
    maximum = np.maximum([2, 3, 4], [1, 5, 2])
    print("np.maximum([2, 3, 4], [1, 5, 2]) =", maximum, ", with a dimension of", maximum.ndim)
    # Output: np.maximum([2, 3, 4], [1, 5, 2]) = [2 5 4] , with a dimension of 1
