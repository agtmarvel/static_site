#class instance creation
class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props
	
	#methods
	def to_html(self):
		raise NotImplementedError

	def props_to_html(self):
		if not self.props:
			return ""
		result = ""
		for key, value in self.props.items():
			result += f' {key}="{value}"'
		return result

	def __repr__(self):
		return f"HTMLNode: tag = {self.tag}, value = {self.value}, children = {self.children}, and props = {self.props}"

#child class

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None,  props)
		self.children = []

	def to_html(self):
		if self.value and self.tag is None:
			raise ValueError("Either a tag or a value must be provided")
		if self.value == None:
			raise ValueError("Value cannot be None")
		if self.tag == None:
			return f"{self.value}"
		else:
			props_html = self.props_to_html()
			return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)
		self.children = children
		if self.value is not None:
			raise ValueError("ParentNode cannot have a 'value'. Use children instead.")
	def to_html(self):
		if self.tag is None:
			raise ValueError("Tag cannot be None")
		if not self.children:
			raise ValueError("Children cannot be empty for a parent node")
		props_html = self.props_to_html() if hasattr(self, 'props_to_html') else ""
		html = f"<{self.tag}{props_html}>"
		for child in self.children:
			html += child.to_html()
		html += f"</{self.tag}>"
		return html
