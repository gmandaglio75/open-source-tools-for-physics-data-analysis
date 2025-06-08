 import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)

    # Calculate the cumulative sum
    print("\nCalculate the cumulative sum by means of the np.cumsum() function")
    #Aggregating one dimensional arrays
    cumsum1 = np.cumsum(one_d)
    print("np.cumsum(one_d) =", cumsum1, ", with a dimension of", cumsum1.ndim)
    # Output: np.cumsum(one_d) = [1 3] , with a dimension of 1
    #Aggregating two dimensional arrays
    cumsum2 = np.cumsum(two_d)
    print("np.cumsum(two_d) =", cumsum2, ", with a dimension of", cumsum2.ndim)
    # Output: np.cumsum(two_d) = [ 3  7 12 18] , with a dimension of 1
    cumsum2_0 = np.cumsum(two_d, axis = 0)
    print("np.cumsum(two_d, axis = 0) =", cumsum2_0, ", with a dimension of", cumsum2_0.ndim)
    # Output: np.cumsum(two_d, axis = 0) = [[ 3  4] [ 8 10]] , with a dimension of 2
    cumsum2_1 = np.cumsum(two_d, axis = 1)
    print("np.cumsum(two_d, axis = 1) =", cumsum2_1, ", with a dimension of", cumsum2_1.ndim)
    # Output: np.cumsum(two_d, axis = 1) = [[ 3  7] [ 5 11]] , with a dimension of 2
    #Aggregating three dimensional arrays
    cumsum3 = np.cumsum(three_d)
    print("np.cumsum(three_d) =", cumsum3, ", with a dimension of", cumsum3.ndim)
    # Output: np.cumsum(three_d) = [ 7 15 24 34 45 57 70 84] , with a dimension of 1
    cumsum3_0 = np.cumsum(three_d, axis = 0)
    print("np.cumsum(three_d, axis = 0) =", cumsum3_0, ", with a dimension of", cumsum3_0.ndim)
    # Output: np.cumsum(three_d, axis = 0) = [[[ 7  8] [ 9 10]] [[18 20] [22 24]]] , with a dimension of 3
    cumsum3_1 = np.cumsum(three_d, axis = 1)
    print("np.cumsum(three_d, axis = 1) =", cumsum3_1, ", with a dimension of", cumsum3_1.ndim)
    # Output: np.cumsum(three_d, axis = 1) = [[[ 7  8] [16 18]] [[11 12] [24 26]]] , with a dimension of 3
    cumsum3_2 = np.cumsum(three_d, axis = 2)
    print("np.cumsum(three_d, axis = 2) =", cumsum3_2, ", with a dimension of", cumsum3_2.ndim)
    # Output: np.cumsum(three_d, axis = 2) = [[[ 7 15] [ 9 19]] [[11 23] [13 27]]] , with a dimension of 3
    
    # Calculate the cumulative product
    print("\nCalculate the cumulative product by means of the np.cumprod() function")
    #Aggregating one dimensional arrays
    cumprod1 = np.cumprod(one_d)
    print("np.cumprod(one_d) =", cumprod1, ", with a dimension of", cumprod1.ndim)
    # Output: np.cumprod(one_d) = [1 2] , with a dimension of 1
    #Aggregating two dimensional arrays
    cumprod2 = np.cumprod(two_d)
    print("np.cumprod(two_d) =", cumprod2, ", with a dimension of", cumprod2.ndim)
    # Output: np.cumprod(two_d) = [  3  12  60 360] , with a dimension of 1
    cumprod2_0 = np.cumprod(two_d, axis = 0)
    print("np.cumprod(two_d, axis = 0) =", cumprod2_0, ", with a dimension of", cumprod2_0.ndim)
    # Output: np.cumprod(two_d, axis = 0) = [[ 3  4] [15 24]] , with a dimension of 2
    cumprod2_1 = np.cumprod(two_d, axis = 1)
    print("np.cumprod(two_d, axis = 1) =", cumprod2_1, ", with a dimension of", cumprod2_1.ndim)
    # Output: np.cumprod(two_d, axis = 1) = [[ 3 12] [ 5 30]] , with a dimension of 2
    #Aggregating three dimensional arrays
    cumprod3 = np.cumprod(three_d)
    print("np.cumprod(three_d) =", cumprod3, ", with a dimension of", cumprod3.ndim)
    # Output: np.cumprod(three_d) = [        7        56       504      5040     55440    665280   8648640  121080960] , with a dimension of 1
    cumprod3_0 = np.cumprod(three_d, axis = 0)
    print("np.cumprod(three_d, axis = 0) =", cumprod3_0, ", with a dimension of", cumprod3_0.ndim)
    # Output: np.cumprod(three_d, axis = 0) = [[[  7   8] [  9  10]] [[ 77  96] [117 140]]] , with a dimension of 3
    cumprod3_1 = np.cumprod(three_d, axis = 1)
    print("np.cumprod(three_d, axis = 1) =", cumprod3_1, ", with a dimension of", cumprod3_1.ndim)
    # Output: np.cumprod(three_d, axis = 1) = [[[  7   8] [ 63  80]] [[ 11  12] [143 168]]] , with a dimension of 3
    cumprod3_2 = np.cumprod(three_d, axis = 2)
    print("np.cumprod(three_d, axis = 2) =", cumprod3_2, ", with a dimension of", cumprod3_2.ndim)
    # Output: np.cumprod(three_d, axis = 2) = [[[  7  56] [  9  90]] [[ 11 132] [ 13 182]]] , with a dimension of 3
