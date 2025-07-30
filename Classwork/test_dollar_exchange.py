import unittest
import dollar_exchange

class TestDollarFunction(unittest.TestCase):
	def test_that_dollar_is_equivalent_to_naira(self):
		dollar_exchange.dollar_equivalent(600)
		
	def test_that_dollar_return_correct_equivalent_to_naira(self):
		result = dollar_exchange.dollar_equivalent(600)
		self.assertEqual(result,930000)
	def test_that_amount_is_only_in_figues(self):
		self.assertRaises(ValueError, dollar_exchange.dollar_equivalent, "not a number")
 