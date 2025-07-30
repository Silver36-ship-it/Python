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
		
	def test_number_accepts_decimal_numbers(self):
		result = function_snacks.divide_or_square(27.8)
		self.assertEqual(result,2.8)

class TestFutureInvestment(unittest.TestCase):
	def test_future_investment_value(self):
		function_snacks.future_investment(1,2,3)
	
	def test_future_investment_value_calculation(self):
		result = function_snacks.future_investment(100,50,1)
		self.assertEqual(result,12974.63)
		
	def test_that_prinicipal_amount_is_not_string(self):
		self.assertRaises(ValueError,function_snacks.future_investment,"string",34,56)
	
	def test_that_monthly_interestRate_is_not_string(self):	
		self.assertRaises(ValueError,function_snacks.future_investment,23,"string",67)
	
	def test_that_the_year_input_is_not_string(self):
		self.assertRaises(ValueError,function_snacks.future_investment,34,68,"string")

		
				

		