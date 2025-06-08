 import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the product
    print("\nCalculate the product by means of the np.product() function")
    #Aggregating one dimensional arrays
    product1 = np.product(one_d)
    print("np.product(one_d) =", product1, ", with a dimension of", product1.ndim)
    # Output: np.product(one_d) = 2 , with a dimension of 0
    #Aggregating two dimensional arrays
    product2 = np.product(two_d)
    print("np.product(two_d) =", product2, ", with a dimension of", product2.ndim)
    # Output: np.product(two_d) = 360 , with a dimension of 0
    product2_0 = np.product(two_d, axis = 0)
    print("np.product(two_d, axis = 0) =", product2_0, ", with a dimension of", product2_0.ndim)
    # Output: np.product(two_d, axis = 0) = [15 24] , with a dimension of 1
    product2_1 = np.product(two_d, axis = 1)
    print("np.product(two_d, axis = 1) =", product2_1, ", with a dimension of", product2_1.ndim)
    # Output: np.product(two_d, axis = 1) = [12 30] , with a dimension of 1
    #Aggregating three dimensional arrays
    product3 = np.product(three_d)
    print("np.product(three_d) =", product3, ", with a dimension of", product3.ndim)
    # Output: np.product(three_d) = 121080960 , with a dimension of 0
    product3_0 = np.product(three_d, axis = 0)
    print("np.product(three_d, axis = 0) =", product3_0, ", with a dimension of", product3_0.ndim)
    # Output: np.product(three_d, axis = 0) = [[ 77  96] [117 140]] , with a dimension of 2
    product3_1 = np.product(three_d, axis = 1)
    print("np.product(three_d, axis = 1) =", product3_1, ", with a dimension of", product3_1.ndim)
    # Output: np.product(three_d, axis = 1) = [[ 63  80] [143 168]] , with a dimension of 2
    product3_2 = np.product(three_d, axis = 2)
    print("np.product(three_d, axis = 2) =", product3_2, ", with a dimension of", product3_2.ndim)
    # Output: np.product(three_d, axis = 2) = [[ 56  90] [132 182]] , with a dimension of 2
