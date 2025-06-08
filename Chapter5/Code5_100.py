  import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)

    # Calculate the sum
    print("\nCalculate the sum by means of the np.sum() function")
    #Aggregating one dimensional arrays
    sum1 = np.sum(one_d)
    print("np.sum(one_d) =", sum1, ", with a dimension of", sum1.ndim)
    # Output: np.sum(one_d) = 3 , with a dimension of 0
    #Aggregating two dimensional arrays
    sum2 = np.sum(two_d)
    print("np.sum(two_d) =", sum2, ", with a dimension of", sum2.ndim)
    # Output: np.sum(two_d) = 18 , with a dimension of 0
    sum2_0 = np.sum(two_d, axis = 0)
    print("np.sum(two_d, axis = 0) =", sum2_0, ", with a dimension of", sum2_0.ndim)
    # Output: np.sum(two_d, axis = 0) = [ 8 10] , with a dimension of 1
    sum2_1 = np.sum(two_d, axis = 1)
    print("np.sum(two_d, axis = 1) =", sum2_1, ", with a dimension of", sum2_1.ndim)
    # Output: np.sum(two_d, axis = 1) = [ 7 11] , with a dimension of 1
    #Aggregating three dimensional arrays
    sum3 = np.sum(three_d)
    print("np.sum(three_d) =", sum3, ", with a dimension of", sum3.ndim)
    # Output: np.sum(three_d) = 84 , with a dimension of 0
    sum3_0 = np.sum(three_d, axis = 0)
    print("np.sum(three_d, axis = 0) =", sum3_0, ", with a dimension of", sum3_0.ndim)
    # Output: np.sum(three_d, axis = 0) = [[18 20] [22 24]] , with a dimension of 2
    sum3_1 = np.sum(three_d, axis = 1)
    print("np.sum(three_d, axis = 1) =", sum3_1, ", with a dimension of", sum3_1.ndim)
    # Output: np.sum(three_d, axis = 1) = [[16 18] [24 26]] , with a dimension of 2
    sum3_2 = np.sum(three_d, axis = 2)
    print("np.sum(three_d, axis = 2) =", sum3_2, ", with a dimension of", sum3_2.ndim)
    # Output: np.sum(three_d, axis = 2) = [[15 19] [23 27]] , with a dimension of 2
    
