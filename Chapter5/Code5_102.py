 import numpy as np
    
    # Create 1D, 2D and 3D arrays
    print("\nGenerate 1D, 2D and 3D arrays")
    one_d = np.array([1,2])
    print("one_d =\n", one_d)
    two_d = np.array([[3,4],[5,6]])
    print("two_d =\n", two_d)
    three_d = np.array([[[7,8],[9,10]],[[11,12],[13,14]]])
    print("three_d =\n", three_d)
    
    # Calculate the average
    print("\nCalculate the average by means of the np.average() function")
    #Aggregating one dimensional arrays
    average1 = np.average(one_d)
    print("np.average(one_d) =", average1, ", with a dimension of", average1.ndim)
    # Output: np.average(one_d) = 1.5 , with a dimension of 0
    average1_w = np.average(one_d, weights=one_d)
    print("np.average(one_d, weights=one_d) =", average1_w, ", with a dimension of", average1_w.ndim)
    # Output: np.average(one_d, weights=one_d) = 1.6666666666666667 , with a dimension of 0
    #Aggregating two dimensional arrays
    average2 = np.average(two_d)
    print("np.average(two_d) =", average2, ", with a dimension of", average2.ndim)
    # Output: np.average(two_d) = 4.5 , with a dimension of 0
    average2_w = np.average(two_d, weights=two_d)
    print("np.average(two_d, weights=two_d) =", average2_w, ", with a dimension of", average2_w.ndim)
    # Output: np.average(two_d, weights=two_d) = 4.777777777777778 , with a dimension of 0
    average2_0 = np.average(two_d, axis = 0)
    print("np.average(two_d, axis = 0) =", average2_0, ", with a dimension of", average2_0.ndim)
    # Output: np.average(two_d, axis = 0) = [4. 5.] , with a dimension of 1
    average2_0_w = np.average(two_d, axis = 0, weights=two_d)
    print("np.average(two_d, axis = 0, weights=two_d) =", average2_0_w, ", with a dimension of", average2_0_w.ndim)
    # Output: np.average(two_d, axis = 0, weights=two_d) = [4.25 5.2 ] , with a dimension of 1
    average2_1 = np.average(two_d, axis = 1)
    print("np.average(two_d, axis = 1) =", average2_1, ", with a dimension of", average2_1.ndim)
    # Output: np.average(two_d, weights=two_d) = 4.777777777777778 , with a dimension of 0
    average2_1_w = np.average(two_d, axis = 1, weights=two_d)
    print("np.average(two_d, axis = 1, weights=two_d) =", average2_1_w, ", with a dimension of", average2_1_w.ndim)
    # Output: np.average(two_d, weights=two_d) = 4.777777777777778 , with a dimension of 0
    #Aggregating three dimensional arrays
    average3 = np.average(three_d)
    print("np.average(three_d) =", average3, ", with a dimension of", average3.ndim)
    # Output:np.average(three_d) = 10.5 , with a dimension of 0
    average3_w = np.average(three_d, weights=three_d)
    print("np.average(three_d, weights=three_d) =", average3_w, ", with a dimension of", average3_w.ndim)
    # Output: np.average(three_d, weights=three_d) = 11.0 , with a dimension of 0
    average3_0 = np.average(three_d, axis = 0)
    print("np.average(three_d, axis = 0) =", average3_0, ", with a dimension of", average3_0.ndim)
    # Output: np.average(three_d, axis = 0) = [[ 9. 10.] [11. 12.]] , with a dimension of 2
    average3_0_w = np.average(three_d, axis = 0, weights=three_d)
    print("np.average(three_d, axis = 0, weights=three_d) =", average3_0_w, ", with a dimension of", average3_0_w.ndim)
    # Output: np.average(three_d, axis = 0, weights=three_d) = [[ 9.44444444 10.4       ] [11.36363636 12.33333333]] , with a dimension of 2
    average3_1 = np.average(three_d, axis = 1)
    print("np.average(three_d, axis = 1) =", average3_1, ", with a dimension of", average3_1.ndim)
    # Output: np.average(three_d, axis = 1) = [[ 8.  9.] [12. 13.]] , with a dimension of 2
    average3_1_w = np.average(three_d, axis = 1, weights=three_d)
    print("np.average(three_d, axis = 1, weights=three_d) =", average3_1_w, ", with a dimension of", average3_1_w.ndim)
    # Output: np.average(three_d, axis = 1, weights=three_d) = [[ 8.125       9.11111111] [12.08333333 13.07692308]] , with a dimension of 2
    average3_2 = np.average(three_d, axis = 2)
    print("np.average(three_d, axis = 2) =", average3_2, ", with a dimension of", average3_2.ndim)
    # Output: np.average(three_d, axis = 2) = [[ 7.5  9.5] [11.5 13.5]] , with a dimension of 2
    average3_2_w = np.average(three_d, axis = 2, weights=three_d)
    print("np.average(three_d, axis = 2, weights=three_d) =", average3_2_w, ", with a dimension of", average3_2_w.ndim)
    # Output: np.average(three_d, axis = 2, weights=three_d) = [[ 7.53333333  9.52631579] [11.52173913 13.51851852]] , with a dimension of 2
