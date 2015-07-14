from lxml.etree import fromstring
import json
import requests

class HTMLParser(object):

	def __init__(self, url, selector, spec):
		"""
		url: string, URL to be retrieved
		selector: string, XPath(?)
		spec: dict, dict with values as new selectors
		"""
		self.url = url
		self.selector = selector
		self.spec = spec


	def _request(self):
		# return content
		# stash the response object on self...
		response = requests.get(self.url)
		self.response = response
		return response


	def _parse_html(self):
		etree = fromstring(self.response.text)
		datalist = []
		els = etree.findall(self.selector)
		for el in els:
			data = {}
			for key, attr in self.spec.items():
				if attr:
					try:
						value = el.attrib[attr]
					except KeyError:
						value = ''
				else:
					value = el.text
				data[key] = value
			datalist.append(data)
		return datalist


	def get_response_size(self):
		return self.response.size


	def get_data(self):
		# make HTTP request
		self._request()
		# build data, return JSON
		return self._parse_html()
