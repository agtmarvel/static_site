import unittest
from block_types import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
	def test_paragraph(self):
		block = "This is a simple paragraph."
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
	
	def test_heading(self):
		block = "# Heading level 1"
		self.assertEqual(block_to_block_type(block), BlockType.HEADING)
		
		block = "### Heading level 3"
		self.assertEqual(block_to_block_type(block), BlockType.HEADING)

		block = "##### Heading level 5"
		self.assertEqual(block_to_block_type(block), BlockType.HEADING)

	def test_code(self):
		block = "```\nprint('Do I dream?')\n```"
		self.assertEqual(block_to_block_type(block), BlockType.CODE)

	def test_quote(self):
		block = ">From the River to the Sea\n>Palestine will be Free"
		self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

	def test_unordered_list(self):
		block = "- Katekyo Hitman Reborn\n- One Piece\n- Haikkyu"
		self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

	def test_ordered_list(self):
		block = "1. Red Rising\n2. Golden Son\n3. Morning Star"
		self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

	def test_invalid_ordered_list(self):
		block = "1. First item\n3. Second item\n2. Third item"
		self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
	unittest.main()
