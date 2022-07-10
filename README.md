# NUMPY
![alt text](https://numpy.org/doc/stable/_static/numpylogo.svg)

NumPy, which stands for Numerical Python, is a library consisting of multidimensional array objects and a collection of routines for processing those arrays. Using NumPy, mathematical and logical operations on arrays can be performed.

In Numpy, number of dimensions of the array is called rank of the array.A tuple of integers giving the size of the array along each dimension is known as shape of the array. An array class in Numpy is called as ndarray. Elements in Numpy arrays are accessed by using square brackets and can be initialized by using nested Python Lists.
1. Mathematical and Logical Operations
2. Fourier Transform
3. Operation related to linear Algebra

## WHY NUMPY
![alt text](https://miro.medium.com/max/1400/1*HRezxXfsgF-ZS4CXX0i_Fw.jpeg)

### 1. Fixed-Type
In this one specifies dtype to define the size. It uses fewer bytes therefore less memory. No type checking while iterating through the object.
![alt text](https://miro.medium.com/max/1400/1*JuPhEfCfla3jpbKvKVV8JQ.png)

### 2. Continuous Memory
![alt text](https://i.stack.imgur.com/oQQVI.png)

## APPLICATION
1. Mathematical
2. Plotting
3. Backend(Pandas, photography)
4. Machine Learning

## NUMPY ARRAY CREATION
1. Python Structure (List, Tuple)
2. Numpy array creation object (ones, zeros, linspace, arange)
3. Reading from disk
4. Array from bytes
5. Special Library Function (random)

## READABILITY
Need to explain the logic while using it as it is less readable.

## ANATOMY OF ARRAY
In this lesser the dtype more speed factor is gained i.e.  np.int8>>>>np.int64

## MEMORY LAYOUT
Strides - Number of bytes in each dimension while traversing.
E.g. in 3X3 matrix with itemsize = 2 then stride is 6.

## VECTORIZATION
### 1. Uniform Vectorization
![alt text](https://www.labri.fr/perso/nrougier/from-python-to-numpy/data/Textile-Cone-cropped.jpg)
In this all elements share the same computation time while processing. There is no specific time for a particular step.
E.g. Game of Life

### 2. Temporal Vectorization
![alt text](https://www.labri.fr/perso/nrougier/from-python-to-numpy/data/Fractal-Broccoli-cropped.jpg)
 It is very easy to compute, but it can take a very long time because you need to ensure a given number does not diverge. 
E.g. Mandelbrot

### 3. Spatial Vectorization
![alt text](https://www.labri.fr/perso/nrougier/from-python-to-numpy/data/Fugle-cropped.jpg)
Elements share the same computation time but in subgroups.
E.g. Boids(Flock of birds):- separation, alignment, cohesion

## VIEW v/s COPY
1. The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
2. The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

## BEYOND NUMPY
1. Numpy Expression
2. Cython (Optimized Static Compiler)
3. Numba (Speed as written in Python)
4. Theano (Optimized, speed, stability, GPU)
5. PyCUDA (Access CUDA Parallely)
6. PyOpenCL (Access GPU and Massive Parallel)

## SPLIT
In **np.hsplit** and **np.vsplit** we need to define the parameter that divides the array in equal parts otherwise throw error.
In **np.split** it will divide the array and make empty array if split divide is more that elements along particular axis.

## AXIS
1. For 1-D —>
   <br>axis = 0

2. For 2-D —> 
<br>Axis = 0 down the column
<br>Axis = 1 along the row

## Keywords
1. ```np.dtype()```
2. ```np.pad()``` :  The function returns the padded array of rank equal to the given array and the shape will increase according to pad_width.
3. ```np.diag()``` : Diagonal we require; k>0 means diagonal above main diagonal or vice versa.
4. ```defaults = np.seterr(all="ignore")``` : remove all warning.
5. ```np.fromiter()``` : array using generator
6. ```numpy.tile(A, reps)``` : Construct an array by repeating A number of times given by reps.
7. ```np.add.reduce()``` : to add array faster than np.sum() for small array.
8. ```data.flags.writeable = True``` : to make data in readable format.
9. ```np.iinfo, np.finfo``` : limit the machine to integer and float. The kind of integer data type to get information about.
10. ```numpy.set_printoptions(threshold=sys.maxsize)``` : to print all the values
11. ```np.put()``` : used to change values defining data amd index
12. ```np.random.choice``` : used to select number of random values.
13. ```keepdims parameter``` : used to maintain dimensions on np operation like mean etc