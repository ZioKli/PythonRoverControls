import unittest

# All Code Should be written inside these lines
#######################################################################################

# finish writing the subtract function so that it returns the difference between two parameters
# x and y
def subtract(x,y):
    return

#######################################################################################




# this section of code is used to automatically test the function you wrote
class test(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(subtract(5,3), 2)
        self.assertEqual(subtract(213,103), 110)
        self.assertEqual(subtract(0,0), 0)
        self.assertEqual(subtract(1,1), 0)



if __name__ == "__main__":
    unittest.main()