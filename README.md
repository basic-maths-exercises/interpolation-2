# Function for linear interpolation

It is essential to recognize that the method that we used to interpolate the function in the previous exercise as long as we are given a pair of points in the cartesian plane. Given what we have learned about Python functions in the other parts of the exercise, it is thus useful to write a function for doing linear interpolation.  We can then reuse the code that we have written multiple time.

I have started writing this function for you in `main.py`.  As you can see, I have written the beginnings of a function called `linear_interpolation`, which you must complete.  This function has three input variables:

1. `lxvals` - a list of x values at which you would like to evaluate the y-value of the function.
2. `xvals` - a pair of x values at which the value of the function is known
3. `yvals` - the pair of y values that correspond to the x values in xvals

`linear_interpolation` should return an array called `lyvals` that contains the values of the interpolated function for the points in `lxvals`.  __Your task in this exercise is to write the one additional line of code in this function that is required to evaluate the interpolated function using:__

![](https://render.githubusercontent.com/render/math?math=f(x)=f(x_1)%2B\frac{f(x_2)-f(x_1)}{x_2-x_1}(x-x_1))

Notice that I have used the enumerate command here as shown below:

````
for i, x in enumerate(lxvals) : 
   lyvals[i]
````

When a for loop is written in this way:

1.  On the first pass through the loop `i=0` and `x=lxvals[0]`
2. On the second pass through the loop `i=1` and `x=lxvals[1]`
3. On the third pass through the loop `i=2` and `x=lxvals[2]`
4. etc

Once the exercise is completed correctly, a graph showing the linear interpolated values for the functions ![](https://render.githubusercontent.com/render/math?math=x^2), ![](https://render.githubusercontent.com/render/math?math=\exp(x)), ![](https://render.githubusercontent.com/render/math?math=\sin(x)) and ![](https://render.githubusercontent.com/render/math?math=\cos(x)) should appear.
