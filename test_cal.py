import unittest
import cal

class TestCal(unittest.TestCase):
    """
    Test the functions from cal.py file
    """

    def test_add(self):
        """
        Test that the addition of two integers returns the correct data
        """
        result = cal.cal_fun(1,2,"Addition")
        self.assertEqual(result,"3")

    def test_sub(self):
        """
        Test that the subtraction of two integers returns the correct data
        """
        result = cal.cal_fun(5,3,"Subtraction")
        self.assertEqual(result,"2")

    def test_mul(self):
        """
        Test that the multiplication of two integers returns the correct data
        """
        result = cal.cal_fun(2,3,"Multiplication")
        self.assertEqual(result,"6")

    def test_div(self):
        """
        Test that the division of two integers returns the correct data
        """
        result = cal.cal_fun(6,3,"Division")
        self.assertEqual(result,"2")

if __name__ == '__main__':
    unittest.main()

    

    