from split_delimiter import *
import unittest
from textnode import TextNode, TextType

class TestSplitDelimiter(unittest.TestCase):
	def test_split_code_delimiter(self):
        # Test basic code delimiter functionality
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        
		self.assertEqual(len(new_nodes), 3)
		self.assertEqual(new_nodes[0].text, "This is text with a ")
		self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
		self.assertEqual(new_nodes[1].text, "code block")
		self.assertEqual(new_nodes[1].text_type, TextType.CODE)
		self.assertEqual(new_nodes[2].text, " word")
		self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
	
	def test_split_bold_delimiter(self):
        # Test bold delimiter functionality
		node = TextNode("This is text with a **bold phrase** in it", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        
		self.assertEqual(len(new_nodes), 3)
		self.assertEqual(new_nodes[0].text, "This is text with a ")
		self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
		self.assertEqual(new_nodes[1].text, "bold phrase")
		self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
		self.assertEqual(new_nodes[2].text, " in it")
		self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

	def test_multiple_delimiters(self):
		node1 = TextNode("This is the first node and with **bold phrase** in it", TextType.TEXT)
		node2 = TextNode("This is the second and with a `code block` word", TextType.TEXT)

		bold_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
		
		self.assertEqual(len(bold_nodes), 4)
		self.assertEqual(bold_nodes[0].text, "This is the first node and with ")
		self.assertEqual(bold_nodes[0].text_type, TextType.TEXT)
		self.assertEqual(bold_nodes[1].text, "bold phrase")
		self.assertEqual(bold_nodes[1].text_type, TextType.BOLD)
		self.assertEqual(bold_nodes[2].text, " in it")
		self.assertEqual(bold_nodes[2].text_type, TextType.TEXT)
		self.assertEqual(bold_nodes[3].text, "This is the second and with a `code block` word")
		self.assertEqual(bold_nodes[3].text_type, TextType.TEXT)

    # Now test code delimiters on the result of the bold transformation
		final_nodes = split_nodes_delimiter(bold_nodes, "`", TextType.CODE)
    
    # Should have 6 nodes: text, bold, text, text, code, text
		self.assertEqual(len(final_nodes), 6)
    # First 3 nodes should be unchanged from bold_nodes
		self.assertEqual(final_nodes[0].text, "This is the first node and with ")
		self.assertEqual(final_nodes[0].text_type, TextType.TEXT)
		self.assertEqual(final_nodes[1].text, "bold phrase")
		self.assertEqual(final_nodes[1].text_type, TextType.BOLD)
		self.assertEqual(final_nodes[2].text, " in it")
		self.assertEqual(final_nodes[2].text_type, TextType.TEXT)
    # Last 3 nodes should be the result of splitting node2 with code delimiters
		self.assertEqual(final_nodes[3].text, "This is the second and with a ")
		self.assertEqual(final_nodes[3].text_type, TextType.TEXT)
		self.assertEqual(final_nodes[4].text, "code block")
		self.assertEqual(final_nodes[4].text_type, TextType.CODE)
		self.assertEqual(final_nodes[5].text, " word")
		self.assertEqual(final_nodes[5].text_type, TextType.TEXT)


if __name__ == "__main__":
	unittest.main()
