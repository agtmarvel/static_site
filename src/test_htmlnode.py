from htmlnode import HTMLNode

import unittest

class TestHTMLNode(unittest.TestCase):
	def test_props_to_html_empty(self):
		node1 = HTMLNode(props=None)
		self.assertEqual(node1.props_to_html(), "")
	
		node2 = HTMLNode(props={})
		self.assertEqual(node2.props_to_html(), "")

	def test_props_to_html_single_prop(self):
		node = HTMLNode(props={"href": "https://example.com"})
		self.assertEqual(node.props_to_html(), ' href="https://example.com"')

	def test_props_to_html_multiple_props(self):
		node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
		result = node.props_to_html()
		self.assertTrue(' href="https://example.com"' in result)
		self.assertTrue(' target="_blank"' in result)
		self.assertEqual(len(result), len(' href="https://example.com" target="_blank"'))







if __name__ == "__main__":
    unittest.main()
