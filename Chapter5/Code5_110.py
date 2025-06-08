 import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([11,8,19,1])
    print("one_d =\n", one_d)
    two_d = np.array([[6,1,11,8],[7,6,2,15]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,13,8],[9,1,10]],[[11,12,2],[2,13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the percentile
    print("\nCalculate the percentile by means of the np.percentile() function")
    #Aggregating one dimensional arrays
    percentile1_0 = np.percentile(one_d, 0)
    print("np.percentile(one_d, 0) =", percentile1_0, ", with a dimension of", percentile1_0.ndim)
    # Output: np.percentile(one_d, 0) = 1.0 , with a dimension of 0
    percentile1_50 = np.percentile(one_d, 50)
    print("np.percentile(one_d, 50) =", percentile1_50, ", with a dimension of", percentile1_50.ndim)
    # Output: np.percentile(one_d, 50) = 9.5 , with a dimension of 0
    #Aggregating two dimensional arrays
    percentile2_0 = np.percentile(two_d, 0)
    print("np.percentile(two_d, 0) =", percentile2_0, ", with a dimension of", percentile2_0.ndim)
    # Output: np.percentile(two_d, 0) = 1.0 , with a dimension of 0
    percentile2_50 = np.percentile(two_d, 50)
    print("np.percentile(two_d, 50) =", percentile2_50, ", with a dimension of", percentile2_50.ndim)
    # Output: np.percentile(two_d, 50) = 6.5 , with a dimension of 0
    percentile2_0_0 = np.percentile(two_d, 0, axis = 0)
    print("np.percentile(two_d, 0, axis = 0) =", percentile2_0_0, ", with a dimension of", percentile2_0_0.ndim)
    # Output: np.percentile(two_d, 0, axis = 0) = [6. 1. 2. 8.] , with a dimension of 1
    percentile2_50_0 = np.percentile(two_d, 50, axis = 0)
    print("np.percentile(two_d, 50, axis = 0) =", percentile2_50_0, ", with a dimension of", percentile2_50_0.ndim)
    # Output: np.percentile(two_d, 50, axis = 0) = [ 6.5  3.5  6.5 11.5] , with a dimension of 1
    percentile2_0_1 = np.percentile(two_d, 0, axis = 1)
    print("np.percentile(two_d, 0, axis = 1) =", percentile2_0_1, ", with a dimension of", percentile2_0_1.ndim)
    # Output: np.percentile(two_d, 0, axis = 1) = [1. 2.] , with a dimension of 1
    percentile2_50_1 = np.percentile(two_d, 50, axis = 1)
    print("np.percentile(two_d, 50, axis = 1) =", percentile2_50_1, ", with a dimension of", percentile2_50_1.ndim)
    # Output: np.percentile(two_d, 50, axis = 1) = [7.  6.5] , with a dimension of 1
    #Aggregating three dimensional arrays
    percentile3_0 = np.percentile(three_d, 0)
    print("np.percentile(three_d, 0) =", percentile3_0, ", with a dimension of", percentile3_0.ndim)
    # Output: np.percentile(three_d, 0) = 1.0 , with a dimension of 0
    percentile3_50 = np.percentile(three_d, 50)
    print("np.percentile(three_d, 50) =", percentile3_50, ", with a dimension of", percentile3_50.ndim)
    # Output: np.percentile(three_d, 50) = 9.5 , with a dimension of 0
    percentile3_0_0 = np.percentile(three_d, 0, axis = 0)
    print("np.percentile(three_d, 0, axis = 0) =", percentile3_0_0, ", with a dimension of", percentile3_0_0.ndim)
    # Output: np.percentile(three_d, 0, axis = 0) = [[ 7. 12.  2.] [ 2.  1. 10.]] , with a dimension of 2
    percentile3_50_0 = np.percentile(three_d, 50, axis = 0)
    print("np.percentile(three_d, 50, axis = 0) =", percentile3_50_0, ", with a dimension of", percentile3_50_0.ndim)
    # Output: np.percentile(three_d, 50, axis = 0) = [[ 9.  12.5  5. ] [ 5.5  7.  12. ]] , with a dimension of 2
    percentile3_0_1 = np.percentile(three_d, 0, axis = 1)
    print("np.percentile(three_d, 0, axis = 1) =", percentile3_0_1, ", with a dimension of", percentile3_0_1.ndim)
    # Output: np.percentile(three_d, 0, axis = 1) = [[ 7.  1.  8.] [ 2. 12.  2.]] , with a dimension of 2
    percentile3_50_1 = np.percentile(three_d, 50, axis = 1)
    print("np.percentile(three_d, 50, axis = 1) =", percentile3_50_1, ", with a dimension of", percentile3_50_1.ndim)
    # Output: np.percentile(three_d, 50, axis = 1) = [[ 8.   7.   9. ] [ 6.5 12.5  8. ]] , with a dimension of 2
    percentile3_0_2 = np.percentile(three_d, 0, axis = 2)
    print("np.percentile(three_d, 0, axis = 2) =", percentile3_0_2, ", with a dimension of", percentile3_0_2.ndim)
    # Output: np.percentile(three_d, 0, axis = 2) = [[7. 1.] [2. 2.]] , with a dimension of 2
    percentile3_50_2 = np.percentile(three_d, 50, axis = 2)
    print("np.percentile(three_d, 50, axis = 2) =", percentile3_50_2, ", with a dimension of", percentile3_50_2.ndim)
    # Output: np.percentile(three_d, 50, axis = 2) = [[ 8.  9.] [11. 13.]] , with a dimension of 2
