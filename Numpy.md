###1. numpy.concatenate
       a = np.array([[1, 2], [3, 4]])
       b = np.array([[5, 6]])
       np.concatenate((a, b), axis=0)
       array([[1, 2],
              [3, 4],
              [5, 6]])

###2. Add image follows:
       output_image[point[1]:point[1] + image_2.shape[0],
             point[0]:point[0] + image_2.shape[1]] = image_2
             
###3.Sorting, searching, and counting
       https://docs.scipy.org/doc/numpy-1.11.0/reference/routines.sort.html

###Solve Linear Algebra

x = np.dot(np.linalg.pinv(mat_A),mat_b)
