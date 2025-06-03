from extract_links import *
import unittest
from enum import Enum
from textnode import *

class ExtractTests(unittest.TestCase):
	def test_extract_mark_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")], matches)
	def test_extract_multiple_markdown_images(self):
		markdown_text = "Here's ![first](https://example.com/first.jpg) and another ![second](https://example.com/second.png)"
		matches = extract_markdown_images(markdown_text)
		self.assertListEqual([
			("first", TextType.IMAGE, "https://example.com/first.jpg"),
			("second", TextType.IMAGE, "https://example.com/second.png")
		], matches)
	def test_extract_markdown_links(self):
		matches = extract_markdown_links(
			"This is text with a link [to boot dev](https://www.boot.dev)"
		)
		self.assertListEqual([("to boot dev", TextType.LINK, "https://www.boot.dev")], matches)
	def test_extract_multiple_markdown_links(self):
		matches = extract_markdown_links(
			"Links to [site one](https://example.com) and [site two](https://example.org)"
		)
		self.assertListEqual([
			("site one", TextType.LINK, "https://example.com"),
			("site two", TextType.LINK, "https://example.org")
		], matches)
	def test_extract_markdown_links_and_images(self):
		matches = extract_markdown_links(
			"A [link](https://example.com) and an ![image](https://example.com/img.jpg)"
		)
		self.assertListEqual([("link", TextType.LINK, "https://example.com")], matches)
		matches = extract_markdown_images(
			"A [link](https://example.com) and an ![image](https://example.com/img.jpg)"
		)
		self.assertListEqual([("image", TextType.IMAGE, "https://example.com/img.jpg")], matches)

class SplitImagesLinks(unittest.TestCase):
	def test_split_no_img(self):
		node = TextNode("This is text with no images", TextType.TEXT)
		result = split_nodes_image([node])
		self.assertEqual(1, len(result))
		self.assertEqual(node, result[0])

	def test_split_no_link(self):
		node = TextNode("This is text with no links", TextType.TEXT)
		result = split_nodes_link([node])
		self.assertEqual(1, len(result))
		self.assertEqual(node, result[0])

	def test_split_single_image(self):
		node = TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) isn't that cool?!", TextType.TEXT,)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" isn't that cool?!", TextType.TEXT),
			], new_nodes,
		)

	def test_split_single_link(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and the link is cool!", TextType.TEXT,)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a link ", TextType.TEXT),
				TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
				TextNode(" and the link is cool!", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_imgs(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
			],
			new_nodes,
		)

	def test_split_single_image_at_end(self):
		node = TextNode(
			"This is text with a picture at the end: ![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT,
		)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("This is text with a picture at the end: ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
			],
			new_nodes,
		)

	def test_split_single_link_at_end(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev)", TextType.TEXT,)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("This is text with a link ", TextType.TEXT),
				TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),],
			new_nodes,
		)

	def test_split_image_beginning(self):
		node = TextNode("![image](https://i.imgur.com/zjjcJKZ.png) is a neat-o image", TextType.TEXT,)
		new_nodes = split_nodes_image([node])
		self.assertListEqual(
			[
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" is a neat-o image", TextType.TEXT),
			],
			new_nodes,
		)

	def test_split_link_beginning(self):
		node = TextNode("[to boot dev](https://www.boot.dev) is a great link", TextType.TEXT,)
		new_nodes = split_nodes_link([node])
		self.assertListEqual(
			[
				TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
				TextNode(" is a great link", TextType.TEXT),
			],
			new_nodes,
		)


	def test_split_links_and_images(self):
		node = TextNode("A [link](https://example.com) and an ![image](https://example.com/img.jpg)", TextType.TEXT)
		new_nodes = split_nodes_image(split_nodes_link([node]))
		
		self.assertEqual(4, len(new_nodes))

		self.assertEqual("A ", new_nodes[0].text)
		self.assertEqual(TextType.TEXT, new_nodes[0].text_type)
		
		self.assertEqual("link", new_nodes[1].text)
		self.assertEqual(TextType.LINK, new_nodes[1].text_type)
		self.assertEqual("https://example.com", new_nodes[1].url)
		
		self.assertEqual(" and an ", new_nodes[2].text)
		self.assertEqual(TextType.TEXT, new_nodes[2].text_type)

		self.assertEqual("image", new_nodes[3].text)
		self.assertEqual(TextType.IMAGE, new_nodes[3].text_type)
		self.assertEqual("https://example.com/img.jpg", new_nodes[3].url)

#Block tests
def test_markdown_to_blocks(self):
	md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
	blocks = markdown_to_blocks(md)
	self.assertEqual(
		blocks,
		[
			"This is **bolded** paragraph",
			"This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
			"- This is a list\n- with items",
		],
	)

def test_markdown_to_blocks_with_broken_link(self):
	md = """
This is a paragraph

This paragraph has an image [image] https://exam
ple.com/img.jpg

Another paragraph
"""
	blocks = markdown_to_blocks(md)
	self.assertEqual(
		blocks,
		[
			"This is a paragraph",
			"This paragraph has an image [image] https://exam\nple.com/img.jpg",
			"Another paragraph"
		]
	)

#test markdown title
def test_title_missing_raises(self):
	with self.assertRaises(Exception):
		extract_title("Superman")

def test_title(self):
	matches = extract_title("# Superman")
	self.assertEqual(
		matches,
		"Superman"
	)

def test_sub_title(self):
	with self.assertRaises(Exception):
		extract_title("## Smashes the Klan")

if __name__ == "__main__":
    unittest.main()

