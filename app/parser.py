from bs4 import BeautifulSoup
import json
import requests

class HTMLParser(object):

	def __init__(self, url, autorequest=True):
		"""
		url: string, URL to be retrieved
		"""
		self.url = url
		if autorequest:
			self._request()

	def _request(self):
		"""
		initialises the request
		stashes the entire response object on self
		returns the content
		"""
		response = requests.get(self.url)
		if response.ok:
			self.response = response
			return response.content
		else:
			return None

	def get_data(self, selector, spec):
		"""
		parse the HTML based on the spec
		"""
		doc = BeautifulSoup(self.response.text, 'html.parser')
		datalist = []
		els = doc.select(selector)
		for el in els:
			data = {}
			for key, attr in spec.items():
				if attr:
					value = el.attrs.get(attr, '')
				else:
					value = el.text.strip()
				data[key] = value
			datalist.append(data)
		return datalist


	def get_response_size(self):
		"""
		returns size of the response in Kb.
		some http headers don't offer the content-size if the response is chunked
		in that case we'll return the length of the content as a best guess
		"""
		try:
			size = self.response.headers['content-length']
		except KeyError:
			size = len(self.response.content)
		return size