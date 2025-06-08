import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the mean
    print("\nCalculate the mean by means of the np.mean() function")
    #Aggregating one dimensional arrays
    mean1 = np.mean(one_d)
    print("np.mean(one_d) =", mean1, ", with a dimension of", mean1.ndim)
    # Output: np.mean(one_d) = 1.5 , with a dimension of 0
    #Aggregating two dimensional arrays
    mean2 = np.mean(two_d)
    print("np.mean(two_d) =", mean2, ", with a dimension of", mean2.ndim)
    # Output: np.mean(two_d) = 4.5 , with a dimension of 0
    mean2_0 = np.mean(two_d, axis = 0)
    print("np.mean(two_d, axis = 0) =", mean2_0, ", with a dimension of", mean2_0.ndim)
    # Output: np.mean(two_d, axis = 0) = [4. 5.] , with a dimension of 1
    mean2_1 = np.mean(two_d, axis = 1)
    print("np.mean(two_d, axis = 1) =", mean2_1, ", with a dimension of", mean2_1.ndim)
    # Output: np.mean(two_d, axis = 1) = [3.5 5.5] , with a dimension of 1
    #Aggregating three dimensional arrays
    mean3 = np.mean(three_d)
    print("np.mean(three_d) =", mean3, ", with a dimension of", mean3.ndim)
    # Output: np.mean(three_d) = 10.5 , with a dimension of 0
    mean3_0 = np.mean(three_d, axis = 0)
    print("np.mean(three_d, axis = 0) =", mean3_0, ", with a dimension of", mean3_0.ndim)
    # Output: np.mean(three_d, axis = 0) = [[ 9. 10.] [11. 12.]] , with a dimension of 2
    mean3_1 = np.mean(three_d, axis = 1)
    print("np.mean(three_d, axis = 1) =", mean3_1, ", with a dimension of", mean3_1.ndim)
    # Output: np.mean(three_d, axis = 1) = [[ 8.  9.] [12. 13.]] , with a dimension of 2
    mean3_2 = np.mean(three_d, axis = 2)
    print("np.mean(three_d, axis = 2) =", mean3_2, ", with a dimension of", mean3_2.ndim)
    # Output: np.mean(three_d, axis = 2) = [[ 7.5  9.5] [11.5 13.5]] , with a dimension of 2
