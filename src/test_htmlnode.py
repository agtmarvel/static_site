from htmlnode import *

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


class TestLeafNode(unittest.TestCase):
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
	def test_leaf_to_html_props(self):
		node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
	def test_leaf_to_html_bold(self):
		node = LeafNode("b", "This text is bold!")
		self.assertEqual(node.to_html(), "<b>This text is bold!</b>")
	def test_leaf_to_html_value_none(self):
		node = LeafNode("p", None)
		with self.assertRaises(ValueError):
			node.to_html()
	def test_leaf_to_html_tag_none(self):
		node = LeafNode(None, "What no tag?")
		with self.assertRaises(ValueError):
			node.to_html()


class TestParentNode(unittest.TestCase):
	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>",)
	def test_to_html_no_children(self):
		parent_node = ParentNode("div", [])
		with self.assertRaises(ValueError):
			parent_node.to_html()
	def test_to_html_no_tag(self):
		child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		parent_node = ParentNode(None, [child_node])
		with self.assertRaises(ValueError):
			parent_node.to_html()
	def test_to_html_with_props(self):
		child_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), '<div><a href="https://www.google.com">Click me!</a></div>')
	def test_to_html_with_multiple_children(self):
		child_node_1 = LeafNode("span", "first child")
		child_node_2 = LeafNode("b", "second child")
		parent_node = ParentNode("div", [child_node_1, child_node_2])
		self.assertEqual(parent_node.to_html(), "<div><span>first child</span><b>second child</b></div>")


if __name__ == "__main__":
    unittest.main()
