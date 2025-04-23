from htmlnode import *
from textnode import *
from split_delimiter import *
import re
import unittests

def extract_markdown_images(text):
	
	pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
	
	matches = re.findall(r"your_pattern", text)
	return matches

def extract_markdown_links(text):
	
	pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
	
	matches = re.findall(r"your_pattern", text)
	return matches

#tests

class ExtractTests(unittest.TestCase):
	def test_extract_mark_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

	def test_extract_multiple_markdown_images(self):
		self.assertListEqual([
			("first", "https://example.com/first.jpg"),
			("second", "https://example.com/second.png")
		], matches)

	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			"This is text with a link [to boot dev](https://www.boot.dev)"
		)
		self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

	def test_extract_multiple_markdown_links(self):
		matches = extract_markdown_links(
			"Links to [site one](https://example.com) and [site two](https://example.org)"
		)
		self.assertListEqual([
			("site one", "https://example.com"),
			("site two", "https://example.org")
		], matches)

	def test_extract_markdown_links_and_images(self):
		matches = extract_markdown_links(
			"A [link](https://example.com) and an ![image](https://example.com/img.jpg)"
		)
		self.assertListEqual([("link", "https://example.com")], matches)
		matches = extract_markdown_images(
			"A [link](https://example.com) and an ![image](https://example.com/img.jpg)"
		)
		self.assertListEqual([("image", "https://example.com/img/jpg)], matches)


if __name__ == "__main__":
    unittest.main()
