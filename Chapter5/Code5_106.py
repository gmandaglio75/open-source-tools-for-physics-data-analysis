    import numpy as np

    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([11,8,19,1])
    print("one_d =\n", one_d)
    two_d = np.array([[6,1,11,8],[7,6,2,15]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,13,8],[9,1,10]],[[11,12,2],[2,13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the median
    print("\nCalculate the median by means of the np.median() function")
    #Aggregating one dimensional arrays
    median1 = np.median(one_d)
    print("np.median(one_d) =", median1, ", with a dimension of", median1.ndim)
    # Output: np.median(one_d) = 9.5 , with a dimension of 0
    #Aggregating two dimensional arrays
    median2 = np.median(two_d)
    print("np.median(two_d) =", median2, ", with a dimension of", median2.ndim)
    # Output: np.median(two_d) = 6.5 , with a dimension of 0
    median2_0 = np.median(two_d, axis = 0)
    print("np.median(two_d, axis = 0) =", median2_0, ", with a dimension of", median2_0.ndim)
    # Output: np.median(two_d, axis = 0) = [ 6.5  3.5  6.5 11.5] , with a dimension of 1
    median2_1 = np.median(two_d, axis = 1)
    print("np.median(two_d, axis = 1) =", median2_1, ", with a dimension of", median2_1.ndim)
    # Output: np.median(two_d, axis = 1) = [7.  6.5] , with a dimension of 1
    #Aggregating three dimensional arrays
    median3 = np.median(three_d)
    print("np.median(three_d) =", median3, ", with a dimension of", median3.ndim)
    # Output: np.median(three_d) = 9.5 , with a dimension of 0
    median3_0 = np.median(three_d, axis = 0)
    print("np.median(three_d, axis = 0) =", median3_0, ", with a dimension of", median3_0.ndim)
    # Output: np.median(three_d, axis = 0) = [[ 9.  12.5  5. ] [ 5.5  7.  12. ]] , with a dimension of 2
    median3_1 = np.median(three_d, axis = 1)
    print("np.median(three_d, axis = 1) =", median3_1, ", with a dimension of", median3_1.ndim)
    # np.median(three_d, axis = 1) = [[ 8.   7.   9. ] [ 6.5 12.5  8. ]] , with a dimension of 2
    median3_2 = np.median(three_d, axis = 2)
    print("np.median(three_d, axis = 2) =", median3_2, ", with a dimension of", median3_2.ndim)
    # Output: np.median(three_d, axis = 2) = [[ 8.  9.] [11. 13.]] , with a dimension of 2
