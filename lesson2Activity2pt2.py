import unittest


# This is a function
# the def keyword means that this is the definition of a function with the name add
# that takes in two parameters which are the two variables in the parentheses
# x is the first parameter
# y is the second parameter
# everything following the colon and indented is what the function actually does
# the return keyword gives returns a value to the line of code that called the function
def add(x, y):
    z = x + y
    return z

# All Code Should be written inside these lines
#######################################################################################

# finish writing the subtract function so that it returns the difference between two parameters
# x and y
def subtract(x,y):

    return

#######################################################################################

class test(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(213,103), 110)



if __name__ == "__main__":
    unittest.main()