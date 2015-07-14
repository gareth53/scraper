import unittest
from mock import Mock
from ddt import ddt, data
from .parser import HTMLParser
from .utils import decimalize

@ddt
class TestParser(unittest.TestCase):

	@data(
		{
			'mrkup': "<html><body><ul class='list'><li>this is simple test</li></ul></body></html>",
			'selector': 'ul.list li',
			'spec': { 'text': None },
			'expect': [{ 'text': 'this is simple test' }]
		},
		{
			'mrkup': "<html><body><ul id='myid'><li>test1</li><li>test2</li></ul></body></html>",
			'selector': 'ul#myid li',
			'spec': { 'text': None },
			'expect': [{ 'text': 'test1' }, { 'text': 'test2' }]
		},
		{
			'mrkup': "<html><body><ul><li id='t1'>test1</li><li id='t2'>test2</li></ul></body></html>",
			'selector': 'li#t1, li#t2',
			'spec': {
				'text': None,
				'attr': 'id'
			},
			'expect': [{ 'text': 'test1', 'attr': 't1' }, { 'text': 'test2', 'attr': 't2' }]
		},
		{
			'mrkup': "<html><body><ul><li id='t1' data-id='td1' href='#t1'>test1</li><li id='t2'>test2</li></ul></body></html>",
			'selector': 'li',
			'spec': {
				'data-id': 'data-id',
				'id': 'id',
				'href': 'href'
			},
			'expect': [{ 'data-id': 'td1', 'id': 't1', 'href': '#t1' }, { 'id': 't2', 'data-id': '', 'href': '' }]
		}
	)
	def test_html_parsing(self, data):
		parser = HTMLParser('', False)
		mock_response = Mock()
		mock_response.text = data['mrkup']
		parser.response = mock_response
		assert parser.get_data(data['selector'], data['spec']) == data['expect']


	def test_get_response_size_from_headers(self):
		parser = HTMLParser('', False)
		mock_response = Mock()
		mock_response.headers = { 'content-length': 1234 }
		parser.response = mock_response
		assert parser.get_response_size() == 1234


	def test_get_response_size_from_content(self):
		parser = HTMLParser('', False)
		mock_response = Mock()
		mock_response.headers = {}
		mock_response.content = '1234567890'
		parser.response = mock_response
		assert parser.get_response_size() == 10

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