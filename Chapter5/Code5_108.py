    import numpy as np

    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the std
    print("\nCalculate the std by means of the np.std() function")
    #Aggregating one dimensional arrays
    std1 = np.std(one_d)
    print("np.std(one_d) =", std1, ", with a dimension of", std1.ndim)
    # Output: np.std(one_d) = 0.5 , with a dimension of 0
    #Aggregating two dimensional arrays
    std2 = np.std(two_d)
    print("np.std(two_d) =", std2, ", with a dimension of", std2.ndim)
    # Output: np.std(two_d) = 1.118033988749895 , with a dimension of 0
    std2_0 = np.std(two_d, axis = 0)
    print("np.std(two_d, axis = 0) =", std2_0, ", with a dimension of", std2_0.ndim)
    # Output: np.std(two_d, axis = 0) = [1. 1.] , with a dimension of 1
    std2_1 = np.std(two_d, axis = 1)
    print("np.std(two_d, axis = 1) =", std2_1, ", with a dimension of", std2_1.ndim)
    # Output: np.std(two_d, axis = 1) = [0.5 0.5] , with a dimension of 1
    #Aggregating three dimensional arrays
    std3 = np.std(three_d)
    print("np.std(three_d) =", std3, ", with a dimension of", std3.ndim)
    # Output: np.std(three_d) = 2.29128784747792 , with a dimension of 0
    std3_0 = np.std(three_d, axis = 0)
    print("np.std(three_d, axis = 0) =", std3_0, ", with a dimension of", std3_0.ndim)
    # Output: np.std(three_d, axis = 0) = [[2. 2.] [2. 2.]] , with a dimension of 2
    std3_1 = np.std(three_d, axis = 1)
    print("np.std(three_d, axis = 1) =", std3_1, ", with a dimension of", std3_1.ndim)
    # Output: np.std(three_d, axis = 1) = [[1. 1.] [1. 1.]] , with a dimension of 2
    std3_2 = np.std(three_d, axis = 2)
    print("np.std(three_d, axis = 2) =", std3_2, ", with a dimension of", std3_2.ndim)
    # Output: np.std(three_d, axis = 2) = [[0.5 0.5] [0.5 0.5]] , with a dimension of 2
