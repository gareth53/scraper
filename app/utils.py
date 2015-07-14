

def decimalize(input):
	"""
	takes a number and returns a string in decimal format
	to represent a readable price in GBP and pence
	"""
	flt = str(round(input, 2))
	if flt.find('.') == len(flt) - 2:
		flt = flt + '0'
	return flt