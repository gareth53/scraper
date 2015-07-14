import unittest
from ddt import ddt, data
from .utils import decimalize

@ddt
class TestDecimalizeUtil(unittest.TestCase):
	@data(
		(2, "2.00"),
		(2.5, "2.50"),
		(2.52, "2.52"),
		(2.524, "2.52"),
		(2.525, "2.52"),
		(20, "20.00"),
		(295, "295.00"),
		(9999, "9999.00"),
		(12345, "12345.00"),
	)
	def test_decimalize(self, data):
		assert decimalize(data[0]) == data[1]

if __name__ == '__main__':
    unittest.main()