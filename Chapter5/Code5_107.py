 import numpy as np

    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the variance
    print("\nCalculate the variance by means of the np.var() function")
    #Aggregating one dimensional arrays
    var1 = np.var(one_d)
    print("np.var(one_d) =", var1, ", with a dimension of", var1.ndim)
    # Output: np.var(one_d) = 0.25 , with a dimension of 0
    #Aggregating two dimensional arrays
    var2 = np.var(two_d)
    print("np.var(two_d) =", var2, ", with a dimension of", var2.ndim)
    # Output: np.var(two_d) = 1.25 , with a dimension of 0
    var2_0 = np.var(two_d, axis = 0)
    print("np.var(two_d, axis = 0) =", var2_0, ", with a dimension of", var2_0.ndim)
    # Output: np.var(two_d, axis = 0) = [1. 1.] , with a dimension of 1
    var2_1 = np.var(two_d, axis = 1)
    print("np.var(two_d, axis = 1) =", var2_1, ", with a dimension of", var2_1.ndim)
    # Output: np.var(two_d, axis = 1) = [0.25 0.25] , with a dimension of 1
    #Aggregating three dimensional arrays
    var3 = np.var(three_d)
    print("np.var(three_d) =", var3, ", with a dimension of", var3.ndim)
    # Output: np.var(three_d) = 5.25 , with a dimension of 0
    var3_0 = np.var(three_d, axis = 0)
    print("np.var(three_d, axis = 0) =", var3_0, ", with a dimension of", var3_0.ndim)
    # Output: np.var(three_d, axis = 0) = [[4. 4.] [4. 4.]] , with a dimension of 2
    var3_1 = np.var(three_d, axis = 1)
    print("np.var(three_d, axis = 1) =", var3_1, ", with a dimension of", var3_1.ndim)
    # Output: np.var(three_d, axis = 1) = [[1. 1.] [1. 1.]] , with a dimension of 2
    var3_2 = np.var(three_d, axis = 2)
    print("np.var(three_d, axis = 2) =", var3_2, ", with a dimension of", var3_2.ndim)
    # Output: np.var(three_d, axis = 2) = [[0.25 0.25] [0.25 0.25]] , with a dimension of 2
