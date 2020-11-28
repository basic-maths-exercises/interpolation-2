import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_func_exists(self) :
        self.assertTrue( "linear_interpolator" in globals(), "No function called linear_interpolator has been defined" )

    def test_func_works(self) :
        xv1 = np.linspace(-1,1,2)
        yv1 = np.exp(xv1) 
        interp = linear_interpolator( np.linspace(-1,1,10), xv1, yv1 ) 
        for i,v in enumerate(interp) :
            xv = xv1[0] + (xv1[1]-xv1[0]) / (yv1[1]-yv1[0]) * ( v - yv1[0] ) 
            myx = xv1[0]+i*(xv1[1]-xv1[0]) / (len(interp)-1)
            self.assertTrue( np.abs(xv -myx)<1e-7, "The function for doing linear interpolation does not work" )
        yv1 = np.sin(xv1) 
        interp = linear_interpolator( np.linspace(-1,1,10), xv1, yv1 ) 
        for i,v in enumerate(interp) :
            xv = xv1[0] + (xv1[1]-xv1[0]) / (yv1[1]-yv1[0]) * ( v - yv1[0] ) 
            myx = xv1[0]+i*(xv1[1]-xv1[0]) / (len(interp)-1)
            self.assertTrue( np.abs(xv - myx )<1e-7, "The function for doing linear interpolation does not work" )
