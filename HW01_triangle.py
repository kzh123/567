"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: jrr
"""

import unittest  # this makes Python unittest module available


def classifyTriangle(a, b, c):
    """

    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'


    """
    try:
        x = int(a),
        y = int(b),
        z = int(c),
    except ValueError:
        return "Invalid input"
    else:
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return 'NotATriangle'
        elif a == b and b == c:
            return 'Equilateral'
        elif a == b or a == c or c == b:
            if a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
                return 'Right Isosceles'
            else:
                return 'Isosceles'
        elif a * a + b * b == c * c or a * a + c * c == b * b or b * b + c * c == a * a:
            return 'Right'
        else:
            return 'Scalene'


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ')=', classifyTriangle(a, b, c), sep="")


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self):  # test invalid inputs
        # your tests go here.  Include as many tests as you'd like

        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testMyTestSet2(self):
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle("a", 1, 1), "Invalid input")
        self.assertEqual(classifyTriangle(1, 2, 2.5), "Scalene")
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
        self.assertNotEqual(classifyTriangle(10, 10, 10), 'Isosceles', 'Should be Equilateral')
        self.assertEqual(classifyTriangle(10, 15, 30), 'NotATriangle', 'Should be NotATriangle')


if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1, 2, 3)
    runClassifyTriangle(1, 1, 1)

    unittest.main(exit=False)
