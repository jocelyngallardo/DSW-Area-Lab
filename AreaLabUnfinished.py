import math #math library has pre-written code
import unittest

def circleArea(radius): #defining a function called circleArea and it has a parameter radius
    """Return the area of a circle"""
    return math.pi * radius * radius

def rectArea(base, height):
    """Return the area of a rectangle"""
    return base * height

def trapArea(base1, base2, height):
    """Return the area of a trapezoid"""
    return (base1 + base2)/2 * height

def triArea(base,height):
    """Return the are of a triangle"""
    return (base * height)/2
    
	
class MyTest(unittest.TestCase): #what is going to let us check our code
    def testCircleArea(self):
        self.assertAlmostEqual(circleArea(5), 25*math.pi)
    #def testRectArea(self):
        #self.assertEqual(rectArea(5, 10), 50)
    #def testTrapArea(self):
        #self.assertEqual(trapArea(8, 6, 4), 28)
    #def testTriArea(self):
        #self.assertEqual(triArea(6, 9), 27)
    