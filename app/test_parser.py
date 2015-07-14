import unittest
from mock import Mock
from ddt import ddt, data
from .parser import HTMLParser

# test that _request makes an HTTP _request
# test it stashed the output on the instance
# test _parse_html() method

@ddt
class TestParser(unittest.TestCase):
	
	@data(
		{
			'mrkup': "<html><body><ul><li>this is simple test</li></ul></body></html>",
			'spec': { 'text': None },
			'expect': [{ 'text': 'this is simple test' }]
		},
		{
			'mrkup': "<html><body><ul><li>test1</li><li>test2</li></ul></body></html>",
			'spec': { 'text': None },
			'expect': [{ 'text': 'test1' }, { 'text': 'test2' }]
		},
		{
			'mrkup': "<html><body><ul><li id='t1'>test1</li><li id='t2'>test2</li></ul></body></html>",
			'spec': {
				'text': None,
				'attr': 'id'
			},
			'expect': [{ 'text': 'test1', 'attr': 't1' }, { 'text': 'test2', 'attr': 't2' }]
		},
		{
			'mrkup': "<html><body><ul><li id='t1' data-id='td1' href='#t1'>test1</li><li id='t2'>test2</li></ul></body></html>",
			'spec': {
				'data-id': 'data-id',
				'id': 'id',
				'href': 'href'
			},
			'expect': [{ 'data-id': 'td1', 'id': 't1', 'href': '#t1' }, { 'id': 't2', 'data-id': '', 'href': '' }]
		}
	)
	def test_html_parser_text(self, data):
		parser = HTMLParser('', './/ul/li', data['spec'])
		mock_response = Mock()
		mock_response.text = data['mrkup']
		parser.response = mock_response
		assert parser._parse_html() == data['expect']


if __name__ == '__main__':
    unittest.main()