import matplotlib.pyplot as plt
import numpy as np

def linear_interpolator( lxvals, xvals, yvals ) :
  lyvals = np.zeros(len(lxvals))
  for i, x in enumerate(lxvals) :
    # Your code to set the interpolated values in lyvals goes here 
    lyvals[i] = 
  return lyvals

# Generate the x coordinates of our data points  
xvals = np.linspace( 0, 0.1, 2 )
lxvals = np.linspace(0, 0.1, 10 )

# Generate y values for various different functions
x2vals = xvals*xvals
expvals = np.exp( xvals )
sinvals = np.sin( xvals )
cosvals = np.cos( xvals )

# Make graphs showing the (numerical) derivatives of these functions 
plt.plot( lxvals, linear_interpolator( lxvals, xvals, x2vals), 'b-' )
plt.plot( lxvals, linear_interpolator( lxvals, xvals, expvals), 'r-' )
plt.plot( lxvals, linear_interpolator( lxvals, xvals, sinvals), 'g-' )
plt.plot( lxvals, linear_interpolator( lxvals, xvals, cosvals), 'k-' )
plt.savefig( "interp.png")
