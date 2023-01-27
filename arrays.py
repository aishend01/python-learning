import numpy as np

arr0D = np.array(42)
arr1D = np.array([42, 75, 83])
arr2D = np.array([[52, 65 ,76],[45 ,45, 78]])
arr3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("""Here you have 4 arrays:
number of dimensions: {}
{}
----------
number of dimensions: {}
{}
----------
number of dimensions: {}
{}
----------
number of dimensions: {}
{}
----------
""".format(arr0D.ndim, arr0D, arr1D.ndim, arr1D, arr2D.ndim, arr2D, arr3D.ndim, arr3D))

arr10D = np.array([[[1 ,3, 4],[4, 5 ,6 ]],[[8, 7, 8],[7, 8 ,9]]], ndmin=10)

print(arr10D, "It has {} dimensions".format(arr10D.ndim))
