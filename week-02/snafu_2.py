#! /usr/bin/env python
#
# snafu.py
# This program is hopelessly screwed up - it is an exercise in using the
# debugger
#
#
import math
import pdb
pdb.set_trace()   # for ipython, cpython doesn't need it

def discriminant(A, B, C) :
    """Return the discriminant of the quadratic: B^2-4AC"""
    r = math.sqrt(B*B - 4*A*C)
    return r

def abs_err(a, b):
    return abs(a-b)

def test_function (A, B, C, x, yt, err_limit ) :
    y = A*x*x+B*x+C
    assert abs_err(y, yt) <= err_limit,\
       "The test function returns an incorrect value %f should be %f" % (y, yt)
    return 

#  This is a useless comment
print "Good values to try include 32,16,0, 1,4,3 and 0,16,32"
A = float(raw_input("Enter A "))
B = float(raw_input("Enter B "))
C = float(raw_input("Enter C "))

d = discriminant(A, B, C)
    

r1 = (-B + d)/(2*A)
r2 = (-B - d)/(2*A)
test_function( A, B, C, r1, 0.0, 1.0E-15 )
test_function( A, B, C, r2, 0.0, 1.0E-15 )
                

print "The roots are %f and %f" % ( r1, r2)

          

