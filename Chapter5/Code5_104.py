 import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)

    # Calculate the min
    print("\nCalculate the min value by means of the np.min() function")
    #Aggregating one dimensional arrays
    min1 = np.min(one_d)
    print("np.min(one_d) =", min1, ", with a dimension of", min1.ndim)
    # Output: np.min(one_d) = 1 , with a dimension of 0
    #Aggregating two dimensional arrays
    min2 = np.min(two_d)
    print("np.min(two_d) =", min2, ", with a dimension of", min2.ndim)
    # Output: np.min(two_d) = 3 , with a dimension of 0
    min2_0 = np.min(two_d, axis = 0)
    print("np.min(two_d, axis = 0) =", min2_0, ", with a dimension of", min2_0.ndim)
    # Output: np.min(two_d, axis = 0) = [3 4] , with a dimension of 1
    min2_1 = np.min(two_d, axis = 1)
    print("np.min(two_d, axis = 1) =", min2_1, ", with a dimension of", min2_1.ndim)
    # Output: np.min(two_d, axis = 1) = [3 5] , with a dimension of 1
    #Aggregating three dimensional arrays
    min3 = np.min(three_d)
    print("np.min(three_d) =", min3, ", with a dimension of", min3.ndim)
    # Output: np.min(three_d) = 7 , with a dimension of 0
    min3_0 = np.min(three_d, axis = 0)
    print("np.min(three_d, axis = 0) =", min3_0, ", with a dimension of", min3_0.ndim)
    # Output: np.min(three_d, axis = 0) = [[ 7  8] [ 9 10]] , with a dimension of 2
    min3_1 = np.min(three_d, axis = 1)
    print("np.min(three_d, axis = 1) =", min3_1, ", with a dimension of", min3_1.ndim)
    # np.min(three_d, axis = 1) = [[ 7  8] [11 12]] , with a dimension of 2
    min3_2 = np.min(three_d, axis = 2)
    print("np.min(three_d, axis = 2) =", min3_2, ", with a dimension of", min3_2.ndim)
    # Output: np.min(three_d, axis = 2) = [[ 7  9] [11 13]] , with a dimension of 2
    
    # Calculate the max
    print("\nCalculate the max value by means of the np.max() function")
    #Aggregating one dimensional arrays
    max1 = np.max(one_d)
    print("np.max(one_d) =", max1, ", with a dimension of", max1.ndim)
    # Output: np.max(one_d) = 2 , with a dimension of 0
    #Aggregating two dimensional arrays
    max2 = np.max(two_d)
    print("np.max(two_d) =", max2, ", with a dimension of", max2.ndim)
    # Output: np.max(two_d) = 6 , with a dimension of 0
    max2_0 = np.max(two_d, axis = 0)
    print("np.max(two_d, axis = 0) =", max2_0, ", with a dimension of", max2_0.ndim)
    # Output: np.max(two_d, axis = 0) = [5 6] , with a dimension of 1
    max2_1 = np.max(two_d, axis = 1)
    print("np.max(two_d, axis = 1) =", max2_1, ", with a dimension of", max2_1.ndim)
    # Output: np.max(two_d, axis = 1) = [4 6] , with a dimension of 1
    #Aggregating three dimensional arrays
    max3 = np.max(three_d)
    print("np.max(three_d) =", max3, ", with a dimension of", max3.ndim)
    # Output: np.max(three_d) = 14 , with a dimension of 0
    max3_0 = np.max(three_d, axis = 0)
    print("np.max(three_d, axis = 0) =", max3_0, ", with a dimension of", max3_0.ndim)
    # Output: np.max(three_d, axis = 0) = [[11 12] [13 14]] , with a dimension of 2
    max3_1 = np.max(three_d, axis = 1)
    print("np.max(three_d, axis = 1) =", max3_1, ", with a dimension of", max3_1.ndim)
    # Output: np.max(three_d, axis = 1) = [[ 9 10] [13 14]] , with a dimension of 2
    max3_2 = np.max(three_d, axis = 2)
    print("np.max(three_d, axis = 2) =", max3_2, ", with a dimension of", max3_2.ndim)
    # Output: np.max(three_d, axis = 2) = [[ 8 10] [12 14]] , with a dimension of 2
