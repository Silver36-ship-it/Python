import unittest
import function_snacks
	
class TestFunctionSnacks(unittest.TestCase):
	def test_number_is_divisible_by_5(self):
		function_snacks.divide_or_square(25)
	
	def test_number_is_divisible(self):
		result = function_snacks.divide_or_square(10)
		self.assertEqual(result,3.16)
		
	def test_number_is_not_a_string(self):
		self.assertRaises(ValueError,function_snacks.divide_or_square,"hi")
		
	def test_number_is_not_a_negative_number(self):
		self.assertRaises(ValueError,function_snacks.divide_or_square,-9)

		

		