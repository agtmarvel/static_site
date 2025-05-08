from enum import Enum

class BlockType(Enum):
	PARAGRAPH = "paragraph"
	HEADING = "heading"
	CODE = "code"
	QUOTE = "quote"
	UNORDERED_LIST = "unordered_list"
	ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
	"""
	Determine the type of a markdown block.

	Args:
		block: A string containing a block of markdown text (already stripped)

	Returns:
		The BlockType enum value representing the type of the block
	"""

	lines = block.split("\n")

	if block.startswith(("#", "##", "###", "####", "#####", "######")):
		count = 0
		for char in block:
			if char == '#':
				count += 1
			else:
				break
		if count <= 6 and len(block) > count and block[count] == ' ':
			return BlockType.HEADING
	
	if block.startswith("```") and block.endswith("```"):
		return BlockType.CODE
	
	if all(line.startswith(">") for line in lines):
		return BlockType.QUOTE

	if all(line.startswith("- ") for line in lines):
		return BlockType.UNORDERED_LIST

	if lines:
		is_ordered_list = True
		for i, line in enumerate(lines,1):
			expected_prefix = f"{i}. "
			if not line.startswith(expected_prefix):
				is_ordered_list = False
				break
		if is_ordered_list:
			return BlockType.ORDERED_LIST

	return BlockType.PARAGRAPH

